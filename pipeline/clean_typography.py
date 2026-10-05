import json
import re
import os

def fix_french_typography(text: str) -> str:
    if not isinstance(text, str):
        return text
    
    # Remove soft hyphens
    text = text.replace('\xad', '').replace('\u00ad', '')
    
    # Fix spaces before . and ,
    text = re.sub(r'\s+([.,])', r'\1', text)
    
    # Fix broken apostrophe spacing (e.g. "d' Antigone", "c' est", "l' histoire", "d' un", "n' est")
    text = re.sub(r"([cdjlnmstCDJLNST]|qu|Qu)['’]\s+([a-zA-ZÀ-ÿ])", r"\1'\2", text)
    
    # Fix spaces before closing parenthesis or after opening
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)
    
    # Fix double spaces
    text = re.sub(r'[ \t]{2,}', ' ', text)
    
    return text.strip()

def clean_data_structure(data):
    if isinstance(data, str):
        return fix_french_typography(data)
    elif isinstance(data, list):
        return [clean_data_structure(item) for item in data]
    elif isinstance(data, dict):
        return {k: clean_data_structure(v) for k, v in data.items()}
    return data

def main():
    dirs_to_clean = [
        '1bac-reader/data/boite',
        '1bac-reader/data/condamne',
        '1bac-reader/data/antigone',
        'data/la_boite_a_merveilles',
        'data/le_dernier_jour_dun_condamne',
        'data/antigone'
    ]
    
    for d in dirs_to_clean:
        if not os.path.exists(d):
            continue
        for fname in os.listdir(d):
            if fname.endswith('.json'):
                fpath = os.path.join(d, fname)
                with open(fpath, 'r', encoding='utf-8') as fh:
                    content = json.load(fh)
                cleaned = clean_data_structure(content)
                with open(fpath, 'w', encoding='utf-8') as fh:
                    json.dump(cleaned, fh, ensure_ascii=False, indent=2)
                print(f"Cleaned typography in {fpath}")

if __name__ == '__main__':
    main()
