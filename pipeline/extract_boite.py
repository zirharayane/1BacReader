import sys
import re
from pathlib import Path
import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.utils import clean_text_block, save_json

ROMAN_NUMERALS = {
    'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6,
    'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12
}

def is_page_number(text: str) -> bool:
    return bool(re.match(r'^\s*\d{1,3}\s*$', text))

def extract_boite(pdf_path: Path, output_path: Path) -> dict:
    doc = pymupdf.open(pdf_path)
    chapters = {}
    current_ch = None
    current_paras = []
    
    # Page index 0 is the cover/title page. Chapter 1 starts on page index 1 (Page 2)
    for page_idx in range(1, len(doc)):
        blocks = doc[page_idx].get_text('blocks')
        for b in blocks:
            raw_text = b[4].strip()
            if not raw_text or is_page_number(raw_text):
                continue
            
            # Check for chapter title e.g. "Chapitre I"
            m = re.match(r'^Chapitre\s+([IVXLCDM]+)\s*$', raw_text, re.IGNORECASE)
            if m:
                if current_ch:
                    chapters[current_ch] = current_paras
                roman = m.group(1).upper()
                ch_num = ROMAN_NUMERALS.get(roman, roman)
                current_ch = f"chapitre_{ch_num}"
                current_paras = []
                continue
            
            clean_para = clean_text_block(raw_text)
            if not clean_para:
                continue
            
            # Check if paragraph continues across page boundaries
            if current_paras and not current_paras[-1].endswith(('.', '!', '?', '»', '”', '…', ':', '"', '!»', '?»', '.»')) and (clean_para[0].islower() or current_paras[-1].endswith((',', ';', '-'))):
                current_paras[-1] = current_paras[-1] + ' ' + clean_para
            else:
                current_paras.append(clean_para)
    
    if current_ch:
        chapters[current_ch] = current_paras
    
    save_json(output_path, chapters)
    return chapters

if __name__ == '__main__':
    src = Path('boite.pdf')
    dst = Path('data/la_boite_a_merveilles/chapters.json')
    res = extract_boite(src, dst)
    print(f"Extracted {len(res)} chapters for La Boîte à Merveilles.")
