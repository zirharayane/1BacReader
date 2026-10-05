import sys
import json
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

DATA_DIR = Path("data")

@pytest.fixture(scope="session", autouse=True)
def run_pipeline():
    from pipeline.run_pipeline import main
    main()

def test_all_expected_files_exist():
    expected_files = [
        DATA_DIR / "la_boite_a_merveilles" / "chapters.json",
        DATA_DIR / "la_boite_a_merveilles" / "dictionary.json",
        DATA_DIR / "la_boite_a_merveilles" / "figures.json",
        DATA_DIR / "le_dernier_jour_dun_condamne" / "chapters.json",
        DATA_DIR / "le_dernier_jour_dun_condamne" / "dictionary.json",
        DATA_DIR / "le_dernier_jour_dun_condamne" / "figures.json",
        DATA_DIR / "antigone" / "scenes.json",
        DATA_DIR / "antigone" / "dictionary.json",
        DATA_DIR / "antigone" / "figures.json",
    ]
    for p in expected_files:
        assert p.exists(), f"Missing expected file: {p}"
        assert p.stat().st_size > 50, f"File appears too small or empty: {p}"

def test_boite_chapters_structure():
    path = DATA_DIR / "la_boite_a_merveilles" / "chapters.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert len(data) == 12, f"Expected 12 chapters in La Boîte à Merveilles, got {len(data)}"
    for i in range(1, 13):
        key = f"chapitre_{i}"
        assert key in data, f"Missing {key}"
        assert isinstance(data[key], list), f"{key} value must be a list"
        assert len(data[key]) > 0, f"{key} has no paragraphs"
        for p in data[key]:
            assert isinstance(p, str) and len(p.strip()) > 0
            assert "\ufffd" not in p

def test_hugo_chapters_structure():
    path = DATA_DIR / "le_dernier_jour_dun_condamne" / "chapters.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert len(data) == 49, f"Expected 49 chapters in Le Dernier Jour d'un Condamné, got {len(data)}"
    for i in range(1, 50):
        key = f"chapitre_{i}"
        assert key in data, f"Missing {key}"
        assert isinstance(data[key], list), f"{key} value must be a list"
        assert len(data[key]) > 0, f"{key} has no paragraphs"
        for p in data[key]:
            assert isinstance(p, str) and len(p.strip()) > 0
            assert "\ufffd" not in p

def test_antigone_scenes_structure():
    path = DATA_DIR / "antigone" / "scenes.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert isinstance(data, list), "Antigone scenes.json must be a list"
    assert len(data) > 300, f"Expected > 300 dialogue objects, got {len(data)}"
    
    for item in data:
        assert "speaker" in item and isinstance(item["speaker"], str) and len(item["speaker"]) > 0
        assert "text" in item and isinstance(item["text"], str) and len(item["text"]) > 0
        assert "stage_direction" in item
        if item["stage_direction"] is not None:
            assert isinstance(item["stage_direction"], str)
        assert "\ufffd" not in item["text"]

def test_dictionaries_schema_and_content():
    books = ["la_boite_a_merveilles", "le_dernier_jour_dun_condamne", "antigone"]
    for book in books:
        path = DATA_DIR / book / "dictionary.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        assert isinstance(data, dict), f"{book} dictionary must be a dict"
        assert len(data) >= 10, f"{book} dictionary has too few items ({len(data)})"
        
        for word, info in data.items():
            assert "type" in info, f"Missing 'type' in {book}:{word}"
            assert "fr_def" in info and len(info["fr_def"]) > 0, f"Missing 'fr_def' in {book}:{word}"
            assert "arabic" in info and len(info["arabic"]) > 0, f"Missing 'arabic' in {book}:{word}"
            assert "darija" in info and len(info["darija"]) > 0, f"Missing 'darija' in {book}:{word}"
            assert "english" in info and len(info["english"]) > 0, f"Missing 'english' in {book}:{word}"
            if "infinitive" in info:
                assert isinstance(info["infinitive"], str)

def test_figures_schema_and_content():
    books = ["la_boite_a_merveilles", "le_dernier_jour_dun_condamne", "antigone"]
    for book in books:
        path = DATA_DIR / book / "figures.json"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        assert isinstance(data, list), f"{book} figures must be a list"
        assert len(data) >= 7, f"{book} figures has too few entries ({len(data)})"
        
        for item in data:
            assert "id" in item and len(item["id"]) > 0
            assert "chapter_or_scene" in item and len(item["chapter_or_scene"]) > 0
            assert "quote" in item and len(item["quote"]) > 0
            assert "type" in item and len(item["type"]) > 0
            assert "explanation" in item and len(item["explanation"]) > 0
            assert "arabic" in item and len(item["arabic"]) > 0
            assert "darija" in item and len(item["darija"]) > 0

def test_nlp_figures_detector():
    from pipeline.nlp_figures_detector import detect_figures_in_json
    src = DATA_DIR / "antigone" / "scenes.json"
    detections = detect_figures_in_json(src, "antigone")
    assert len(detections) >= 20
    for d in detections:
        assert "type" in d
        assert "quote" in d
        assert "dialogue_index" in d
