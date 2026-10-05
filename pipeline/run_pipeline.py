import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.extract_boite import extract_boite
from pipeline.extract_hugo import extract_hugo
from pipeline.extract_antigone import extract_antigone
from pipeline.build_dictionary import build_all_dictionaries
from pipeline.build_figures import build_all_figures
from pipeline.nlp_figures_detector import detect_all_works

def main():
    root = Path('.')
    data_dir = root / 'data'
    
    print("=== STARTING 1BAC NLP EXTRACTION PIPELINE ===")
    
    # 1. Extract La Boîte à Merveilles
    boite_pdf = root / 'boite.pdf'
    boite_out = data_dir / 'la_boite_a_merveilles' / 'chapters.json'
    print(f"--> Processing {boite_pdf} ...")
    extract_boite(boite_pdf, boite_out)
    
    # 2. Extract Le Dernier Jour d'un Condamné
    hugo_pdf = root / 'hugo-claude.pdf'
    hugo_out = data_dir / 'le_dernier_jour_dun_condamne' / 'chapters.json'
    print(f"--> Processing {hugo_pdf} ...")
    extract_hugo(hugo_pdf, hugo_out)
    
    # 3. Extract Antigone
    antigone_pdf = root / 'antigone-texte-integral.pdf'
    antigone_out = data_dir / 'antigone' / 'scenes.json'
    print(f"--> Processing {antigone_pdf} ...")
    extract_antigone(antigone_pdf, antigone_out)
    
    # 4. Build Dictionaries
    print("--> Building dictionaries ...")
    build_all_dictionaries(root)
    
    # 5. Build Figures de style (Top 20 Exam Corpus)
    print("--> Building figures de style ...")
    build_all_figures(root)
    
    # 6. Run automated NLP Figure Detector across all 3 texts
    print("--> Running automated NLP figure detector ...")
    detect_all_works(root)
    
    print("=== PIPELINE EXECUTION FINISHED SUCCESSFULLY ===")

if __name__ == '__main__':
    main()
