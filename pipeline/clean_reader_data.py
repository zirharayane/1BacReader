import json
import re
import os

def clean_str(s: str) -> str:
    if not isinstance(s, str):
        return s
    
    # 1. Soft hyphens
    s = s.replace('\xad', '')
    
    # 2. Fix apostrophes represented by \ufffd (e.g. javais, dun, lenfant, cest, soccuper)
    s = re.sub(r"([A-Za-zÀ-ÿ])\ufffd([A-Za-zÀ-ÿ])", r"\1'\2", s)
    
    # 3. Direct word repairs for frequent French terms
    repairs = {
        "Bic\ufffdtre": "Bicêtre",
        "Condamn\ufffd": "Condamné",
        "condamn\ufffd": "condamné",
        "\ufffd mort": "à mort",
        "Voil\ufffd": "Voilà",
        "voil\ufffd": "voilà",
        "pens\ufffde": "pensée",
        "glac\ufffd": "glacé",
        "pr\ufffdsence": "présence",
        "courb\ufffd": "courbé",
        "sant\ufffd": "santé",
        "tr\ufffdve": "trêve",
        "d\ufffdcouvrait": "découvrait",
        "br\ufffdler": "brûler",
        "fra\ufffdche": "fraîche",
        "ineffa\ufffdables": "ineffaçables",
        "amiti\ufffds": "amitiés",
        "\ufffdcole": "école",
        "l\ufffdcole": "l'école",
        "dur\ufffde": "durée",
        "br\ufffdve": "brève",
        "diff\ufffdrents": "différents",
        "r\ufffdve": "rêve",
        "conna\ufffdtre": "connaître",
        "lumi\ufffdre": "lumière",
        "T\ufffdn\ufffdbres": "Ténèbres",
        "ob\ufffdissaient": "obéissaient",
        "sorci\ufffdres": "sorcières",
        "p\ufffdre": "père",
        "m\ufffdre": "mère",
        "rena\ufffdtre": "renaître",
        "p\ufffdch\ufffd": "péché",
        "acc\ufffds": "accès",
        "t\ufffdtes": "têtes",
        "ras\ufffdes": "rasées",
        "vocif\ufffdrations": "vociférations",
        "sacr\ufffds": "sacrés",
        "col\ufffdre": "colère",
        "premi\ufffdre": "première",
        "\ufffdclat\ufffd": "éclaté",
        "d\ufffdcor": "décor",
        "sce'ne": "scène",
        "sc\ufffdne": "scène",
        "r\ufffdle": "rôle",
        "fr\ufffdre": "frère",
        "t\ufffdte": "tête",
        "b\ufffdtise": "bêtise",
        "apr\ufffds": "après",
        "\ufffccoute": "écoute",
        "s\ufffdr": "sûr",
        "bient\ufffdt": "bientôt",
        "d\ufffdj\ufffd": "déjà",
        "m\ufffdme": "même"
    }

    for k, v in repairs.items():
        s = s.replace(k, v)
        
    # Replace any leftover isolated \ufffd with standard apostrophe '
    s = s.replace("\ufffd", "'")
    return s

def clean_data_recursively(obj):
    if isinstance(obj, str):
        return clean_str(obj)
    elif isinstance(obj, list):
        return [clean_data_recursively(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: clean_data_recursively(v) for k, v in obj.items()}
    return obj

def main():
    base = '1bac-reader/data'
    for work in ['boite', 'condamne', 'antigone']:
        work_dir = os.path.join(base, work)
        if not os.path.exists(work_dir):
            continue
        for fname in os.listdir(work_dir):
            if fname.endswith('.json'):
                fpath = os.path.join(work_dir, fname)
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                cleaned = clean_data_recursively(data)
                with open(fpath, 'w', encoding='utf-8') as f:
                    json.dump(cleaned, f, ensure_ascii=False, indent=2)
                print(f"Cleaned {fpath}")

if __name__ == '__main__':
    main()
