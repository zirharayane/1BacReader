import os
import re
import json
from pathlib import Path

def clean_text_block(text: str) -> str:
    """Cleans up raw text blocks from PDF extraction:
    - Removes soft hyphens (\\xad) and rejoins hyphenated word breaks
    - Normalizes multiple spaces and newlines
    - Cleans up common OCR artifacts
    """
    if not text:
        return ""
    
    # Rejoin words broken across lines: e.g. "aujour-\nd'hui" -> "aujourd'hui" or "plu\xad\ntôt" -> "plutôt"
    text = re.sub(r'(\w+)[\xad\-]\n\s*(\w+)', r'\1\2', text)
    # Remove remaining standalone soft hyphens
    text = re.sub(r'[\xad\u00ad]', '', text)
    # Normalize OCR artifact ligatures if any
    text = text.replace('doǻant', 'dormant')
    text = text.replace('sce\'ne', 'scène')
    text = text.replace('Etéoc1e', 'Etéocle')
    text = text.replace('exc1usivement', 'exclusivement')
    text = text.replace('1’encombrait', 'l’encombrait')
    text = text.replace('Creon entreŋ', 'Créon entre,')
    text = text.replace('Ne rއste pas', 'Ne reste pas')
    text = text.replace('Estކce que', 'Est-ce que')
    text = text.replace('vexÚ', 'vexé,')
    text = text.replace('EUe', 'Elle')
    text = text.replace('nÙlÏntenant', 'maintenant')
    
    # Replace internal newlines with single space
    text = re.sub(r'\n+', ' ', text)
    # Collapse multiple whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def save_json(target_path: Path, data: any) -> None:
    """Saves data into a clean, UTF-8 formatted JSON file."""
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {target_path}")
