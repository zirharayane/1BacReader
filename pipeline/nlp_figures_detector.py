import sys
import re
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.utils import clean_text_block
from pipeline.canonical_100_figures import CANONICAL_100_FIGURES

# High-precision linguistic patterns to avoid false positives

ANTONYM_PAIRS = [
    (r'\b(riche|riches)\b', r'\b(pauvre|pauvres)\b'),
    (r'\b(mort|morts|mourir)\b', r'\b(vie|vivant|vivre)\b'),
    (r'\b(jour|matin|aube)\b', r'\b(nuit|soir|crépuscule)\b'),
    (r'\b(noir|noire|sombres)\b', r'\b(blanc|blanche|clairs)\b'),
    (r'\b(dormir|dorment|sommeil)\b', r'\b(veille|éveillé|réveil)\b'),
    (r'\b(pleurer|larmes|pleurs)\b', r'\b(rire|rires|joie)\b'),
    (r'\b(froid|glacé|glaçon)\b', r'\b(chaud|chaleur|flammes|four)\b'),
    (r'\b(libre|liberté)\b', r'\b(captif|prisonnier|enchaîné)\b')
]

OXYMORE_PATTERNS = [
    (r'\bapaisement\s+triste\b', "Oxymore", "Alliance paradoxale de l'apaisement et de la tristesse.", "طباق مجازي يجمع بين السكينة والحزن.", "جمع بين السكون والحزن باش يوصف الخوا والوحشة."),
    (r'\bhideuse\s+fête\b', "Oxymore", "Alliance paradoxale entre la hideur de la torture et la fête.", "طباق تركيبي يجمع بين البشاعة والعيد.", "جمع بين جوج كلمات متناقضين (بشعة وحفلة)."),
    (r'\bsale\s+espoir\b', "Oxymore", "Alliance de mots inversant la valeur positive de l'espoir.", "طباق مجازي يقلب المفاهيم بجعل الأمل قذراً.", "تناقض بليغ كيرد الأمل شي حاجة خانزة."),
    (r'\bobscure\s+clarté\b', "Oxymore", "Opposition entre obscurité et clarté dans le même syntagme.", "طباق يجمع بين الظلمة والنور.", "جمع بين الظلام والضو فالكلمة نفسها."),
    (r'\bsourire\s+glacé\b', "Oxymore", "Alliance contradictoire d'un geste chaleureux et de la glace.", "طباق بين الابتسامة وبرودة الموت.", "تناقض بين الضحكة والبرودة ديال الموت.")
]

COMPARISON_TOOLS = [
    r'\bcomme\s+(?:un|une|des|le|la|les|de|du)\b',
    r'\bpareil(?:s|le|les)?\s+à\b',
    r'\bsemblable(?:s)?\s+à\b',
    r'\btel(?:s|le|les)?\s+qu(?:e|\')\b',
    r'\bressemble(?:nt)?\s+à\b'
]

def norm(text: str) -> str:
    if not text:
        return ""
    text = text.replace("’", "'").replace("`", "'").replace("«", '"').replace("»", '"')
    return re.sub(r'\s+', ' ', text).lower().strip()

class FigureDetector:
    def __init__(self, book_key: str = None):
        self.book_key = book_key
        self.canonical = CANONICAL_100_FIGURES.get(book_key, []) if book_key else []

    def scan_text_segment(self, segment: str, location_id: str, index: int) -> list:
        results = []
        seg_norm = norm(segment)
        
        # 1. Match against Gold-Standard 100 Canonical Exam Figures (100% precision)
        for canon in self.canonical:
            quote_norm = norm(canon["quote"])
            # Check if canonical quote or substantial snippet occurs in segment
            sample = quote_norm[:40] if len(quote_norm) > 40 else quote_norm
            if sample in seg_norm:
                results.append({
                    "id": canon["id"],
                    "chapter_or_scene": location_id,
                    "index": index,
                    "quote": canon["quote"],
                    "type": canon["type"],
                    "detection_source": "verified_canonical_exam_database",
                    "confidence": 1.0,
                    "explanation": canon["explanation"],
                    "arabic": canon["arabic"],
                    "darija": canon["darija"]
                })
                return results # Priority to verified canonical quote

        # 2. Rule-Based NLP Detection for Oxymore
        for pat, fig_type, exp_fr, exp_ar, exp_dar in OXYMORE_PATTERNS:
            m = re.search(pat, segment, re.IGNORECASE)
            if m:
                results.append({
                    "id": f"auto_oxy_{location_id}_{index}",
                    "chapter_or_scene": location_id,
                    "index": index,
                    "quote": m.group(0),
                    "type": fig_type,
                    "detection_source": "rule_based_nlp_engine",
                    "confidence": 0.95,
                    "explanation": exp_fr,
                    "arabic": exp_ar,
                    "darija": exp_dar
                })
                return results

        # 3. Rule-Based NLP Detection for Antithèse
        for w1, w2 in ANTONYM_PAIRS:
            if re.search(w1, segment, re.IGNORECASE) and re.search(w2, segment, re.IGNORECASE):
                results.append({
                    "id": f"auto_anti_{location_id}_{index}",
                    "chapter_or_scene": location_id,
                    "index": index,
                    "quote": segment[:140] + ("..." if len(segment) > 140 else ""),
                    "type": "Antithèse",
                    "detection_source": "rule_based_nlp_engine",
                    "confidence": 0.90,
                    "explanation": f"Opposition lexicale directe au sein de la même phrase.",
                    "arabic": "طباق يقابل بين لفظين متضادين في نفس العبارة.",
                    "darija": "طباق كيقارن بين جوج كلمات متضادين فنفس الجملة."
                })
                return results

        # 4. Rule-Based NLP Detection for Comparaison
        for tool in COMPARISON_TOOLS:
            m = re.search(rf'([^.!?;\n]*{tool}[^.!?;\n]*)', segment, re.IGNORECASE)
            if m:
                matched_span = m.group(1).strip()
                if len(matched_span.split()) >= 4 and len(matched_span.split()) <= 25:
                    results.append({
                        "id": f"auto_comp_{location_id}_{index}",
                        "chapter_or_scene": location_id,
                        "index": index,
                        "quote": matched_span,
                        "type": "Comparaison",
                        "detection_source": "rule_based_nlp_engine",
                        "confidence": 0.88,
                        "explanation": "Présence explicite d'un outil de comparaison liant le comparé au comparant.",
                        "arabic": "تشبيه واضح يربط بين المشبه والمشبه به بأداة مقارنة.",
                        "darija": "تشبيه واضح كيستعمل أداة تشبيه باش يقارن بين جوج حوايج."
                    })
                    return results

        return results

def detect_figures_in_json(input_json_path: Path, book_key: str, output_path: Path = None) -> list:
    with open(input_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    detector = FigureDetector(book_key)
    all_detections = []
    
    # If data is a list of dialogues (e.g. Antigone)
    if isinstance(data, list):
        for idx, item in enumerate(data):
            text = item.get("text", "")
            found = detector.scan_text_segment(text, location_id="dialogue", index=idx)
            for f_item in found:
                f_item["dialogue_index"] = idx
                all_detections.append(f_item)
                
    # If data is a dict of chapters (e.g. Boîte or Hugo)
    elif isinstance(data, dict):
        for ch_key, paragraphs in data.items():
            for idx, p in enumerate(paragraphs):
                found = detector.scan_text_segment(p, location_id=ch_key, index=idx)
                for f_item in found:
                    f_item["paragraph_index"] = idx
                    all_detections.append(f_item)
                    
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(all_detections, f, ensure_ascii=False, indent=2)
        print(f"[OK] Saved {len(all_detections)} detected figures to {output_path}")
        
    return all_detections

def detect_all_works(base_dir: Path):
    data_dir = base_dir / "data"
    
    # 1. Antigone
    ant_src = data_dir / "antigone" / "scenes.json"
    ant_out = data_dir / "antigone" / "detected_figures.json"
    detect_figures_in_json(ant_src, "antigone", ant_out)
    
    # 2. La Boîte à Merveilles
    boite_src = data_dir / "la_boite_a_merveilles" / "chapters.json"
    boite_out = data_dir / "la_boite_a_merveilles" / "detected_figures.json"
    detect_figures_in_json(boite_src, "la_boite_a_merveilles", boite_out)
    
    # 3. Le Dernier Jour d'un Condamné
    hugo_src = data_dir / "le_dernier_jour_dun_condamne" / "chapters.json"
    hugo_out = data_dir / "le_dernier_jour_dun_condamne" / "detected_figures.json"
    detect_figures_in_json(hugo_src, "le_dernier_jour_dun_condamne", hugo_out)

if __name__ == "__main__":
    detect_all_works(Path("."))
