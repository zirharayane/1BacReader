import sys
import re
from pathlib import Path
import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.utils import clean_text_block, save_json

KNOWN_SPEAKERS = [
    'LE PROLOGUE',
    'LA NOURRICE',
    'ANTIGONE',
    'ISMÈNE',
    'HÉMON',
    'CRÉON',
    'LE PREMIER GARDE',
    'LE DEUXIÈME GARDE',
    'LE TROISIÈME GARDE',
    'LE GARDE',
    'LES GARDES',
    'LE CHŒUR',
    'LE CHOEUR',
    'LE MESSAGER',
    'LE PAGE'
]

def is_page_number(text: str) -> bool:
    return bool(re.match(r'^\s*(\d\s*){1,4}\s*$', text))

def extract_antigone(pdf_path: Path, output_path: Path) -> list:
    doc = pymupdf.open(pdf_path)
    dialogues = []
    
    current_speaker = None
    current_stage_dir = []
    current_text_acc = []
    
    def flush_dialogue():
        nonlocal current_speaker, current_stage_dir, current_text_acc
        if current_speaker:
            s_dir = ' '.join(current_stage_dir).strip() if current_stage_dir else None
            text = ' '.join(current_text_acc).strip()
            text = clean_text_block(text)
            if s_dir:
                s_dir = clean_text_block(s_dir).strip('() ')
            if text:
                # Normalize speaker name (e.g. LE CHOEUR -> LE CHŒUR)
                normalized_speaker = "LE CHŒUR" if current_speaker == "LE CHOEUR" else current_speaker
                dialogues.append({
                    "speaker": normalized_speaker,
                    "stage_direction": s_dir if s_dir else None,
                    "text": text
                })
            current_stage_dir = []
            current_text_acc = []
    
    # Text starts at page index 6 (Page 7) and ends at page index 120 (Page 121)
    for page_idx in range(6, 121):
        blocks = doc[page_idx].get_text('blocks')
        for b in blocks:
            raw_text = b[4].strip()
            if not raw_text or is_page_number(raw_text):
                continue
            if 'FIN DE « ANTIGONE »' in raw_text:
                break
            
            # Check if block matches or begins with a known speaker
            lines = [l.strip() for l in raw_text.split('\n') if l.strip()]
            first_line = lines[0]
            
            matched_spk = None
            matched_dir = None
            remainder_lines = []
            
            for spk in KNOWN_SPEAKERS:
                # Match "SPEAKER", "SPEAKER, stage dir", "SPEAKER (stage dir)", "SPEAKER."
                pattern = rf'^{re.escape(spk)}(?:\s*,\s*(.*?)|(?:\s*\((.*?)\))|\s*\.|\s*:)?$'
                m = re.match(pattern, first_line)
                if m:
                    matched_spk = spk
                    # Extract stage direction if present on same line
                    matched_dir = m.group(1) or m.group(2)
                    remainder_lines = lines[1:]
                    break
                
                # Check case where speaker and first speech are on same line
                pattern_inline = rf'^{re.escape(spk)}\s*:\s*(.+)$'
                m_inline = re.match(pattern_inline, first_line)
                if m_inline:
                    matched_spk = spk
                    remainder_lines = [m_inline.group(1)] + lines[1:]
                    break
            
            if matched_spk:
                flush_dialogue()
                current_speaker = matched_spk
                if matched_dir:
                    current_stage_dir.append(matched_dir)
                if remainder_lines:
                    current_text_acc.append('\n'.join(remainder_lines))
            else:
                # Stage direction alone, e.g. "(Elle sort.)" or "Elle va passer."
                if raw_text.startswith('(') and raw_text.endswith(')'):
                    current_stage_dir.append(raw_text)
                elif current_speaker:
                    current_text_acc.append(raw_text)
                else:
                    # Initial stage direction before prologue speaks
                    current_stage_dir.append(raw_text)
    
    flush_dialogue()
    save_json(output_path, dialogues)
    return dialogues

if __name__ == '__main__':
    src = Path('antigone-texte-integral.pdf')
    dst = Path('data/antigone/scenes.json')
    res = extract_antigone(src, dst)
    print(f"Extracted {len(res)} dialogue objects for Antigone.")
