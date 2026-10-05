import sys
import re
from pathlib import Path
import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.utils import clean_text_block, save_json

ROMAN_NUMERALS = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
    'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20,
    'XXI': 21, 'XXII': 22, 'XXIII': 23, 'XXIV': 24, 'XXV': 25, 'XXVI': 26, 'XXVII': 27, 'XXVIII': 28, 'XXIX': 29, 'XXX': 30,
    'XXXI': 31, 'XXXII': 32, 'XXXIII': 33, 'XXXIV': 34, 'XXXV': 35, 'XXXVI': 36, 'XXXVII': 37, 'XXXVIII': 38, 'XXXIX': 39, 'XL': 40,
    'XLI': 41, 'XLII': 42, 'XLIII': 43, 'XLIV': 44, 'XLV': 45, 'XLVI': 46, 'XLVII': 47, 'XLVIII': 48, 'XLIX': 49
}

def is_page_number(text: str) -> bool:
    return bool(re.match(r'^\s*\d{1,3}\s*$', text))

def extract_hugo(pdf_path: Path, output_path: Path) -> dict:
    doc = pymupdf.open(pdf_path)
    chapters = {}
    current_ch = None
    current_paras = []
    
    # Page index 68 (Page 69) is where Chapter I begins
    # Page index 213 (Page 214) is where Chapter XLIX ends
    # Page index 214 (Page 215) starts Claude Gueux which must be excluded
    for page_idx in range(68, 214):
        blocks = doc[page_idx].get_text('blocks')
        for b in blocks:
            raw_text = b[4].strip()
            if not raw_text or is_page_number(raw_text):
                continue
            
            lines = [l.strip() for l in raw_text.split('\n') if l.strip()]
            first_line = lines[0]
            
            if first_line in ROMAN_NUMERALS:
                if current_ch:
                    chapters[current_ch] = current_paras
                ch_num = ROMAN_NUMERALS[first_line]
                current_ch = f"chapitre_{ch_num}"
                current_paras = []
                
                # If there's text after the roman numeral in the same block
                rest_lines = lines[1:]
                if rest_lines:
                    clean_rest = clean_text_block('\n'.join(rest_lines))
                    if clean_rest:
                        current_paras.append(clean_rest)
                continue
            
            clean_para = clean_text_block(raw_text)
            if not clean_para:
                continue
            
            # Paragraph continuity across page breaks
            if current_paras and not current_paras[-1].endswith(('.', '!', '?', '»', '”', '…', ':', '"', '!»', '?»', '.»')) and (clean_para[0].islower() or current_paras[-1].endswith((',', ';', '-'))):
                current_paras[-1] = current_paras[-1] + ' ' + clean_para
            else:
                current_paras.append(clean_para)
    
    if current_ch:
        chapters[current_ch] = current_paras
    
    save_json(output_path, chapters)
    return chapters

if __name__ == '__main__':
    src = Path('hugo-claude.pdf')
    dst = Path('data/le_dernier_jour_dun_condamne/chapters.json')
    res = extract_hugo(src, dst)
    print(f"Extracted {len(res)} chapters for Le Dernier Jour d'un Condamné.")
