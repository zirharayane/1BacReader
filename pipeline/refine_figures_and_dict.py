# -*- coding: utf-8 -*-
"""
Refine figure quotes to exact clauses and add Chapitre 1 missing vocabulary.
"""
import json
import os

NEW_CH1_WORDS = {
    "benjoin": {
        "type": "nom masculin",
        "fr_def": "Résine aromatique brûlée comme encens.",
        "arabic": "بخور الجاوي",
        "darija": "الجاوي",
        "english": "Benzoin incense"
    },
    "crotales": {
        "type": "nom féminin pluriel",
        "fr_def": "Instruments de percussion en fer (qraqeb).",
        "arabic": "صنوج حديدية (القراقب)",
        "darija": "القراقب ديال كناوة",
        "english": "Iron castanets / qraqeb"
    },
    "guimbris": {
        "type": "nom masculin pluriel",
        "fr_def": "Luth traditionnel à cordes des Gnaouas.",
        "arabic": "الكمبري (آلة وترية كناوية)",
        "darija": "الكمبري / الهجهوج",
        "english": "Gimbri / Gnawa lute"
    },
    "morne": {
        "type": "adjectif",
        "fr_def": "Triste, sombre, sans entrain.",
        "arabic": "كئيب وحزين",
        "darija": "كئيب / مغبر",
        "english": "Gloomy / dull"
    },
    "flamboyant": {
        "type": "adjectif",
        "fr_def": "Éclatant comme une flamme.",
        "arabic": "فائق اللمعان كاللهب",
        "darija": "كيبري بحال العافية",
        "english": "Blazing / flaming"
    },
    "confrérie": {
        "type": "nom féminin",
        "fr_def": "Association religieuse ou spirituelle (ex. Gnaouas).",
        "arabic": "طريقة أو زاوية صوفية",
        "darija": "طريقة / طائفة (بحال كناوة)",
        "english": "Brotherhood / order"
    }
}

EXACT_FIGURE_CLAUSE_REPLACEMENTS = {
    "Le soir, quand tous dorment, les riches dans leurs chaudes couvertures, les pauvres sur les marches des boutiques ou sous les porches des palais, moi je ne dors pas.":
        "les riches dans leurs chaudes couvertures, les pauvres sur les marches des boutiques",
    "Ma solitude ne date pas d'hier.": "Ma solitude ne date pas d'hier",
    "Je songe à ma solitude et j'en sens tout le poids.": "j'en sens tout le poids",
    "Moi, je ne voulais rien imiter, je voulais connaître.": "je ne voulais rien imiter, je voulais connaître",
}

def update_dictionary():
    dict_paths = [
        'data/la_boite_a_merveilles/dictionary.json',
        '1bac-reader/data/boite/dictionary.json'
    ]
    for dp in dict_paths:
        if os.path.exists(dp):
            with open(dp, 'r', encoding='utf-8') as f:
                d = json.load(f)
            for k, v in NEW_CH1_WORDS.items():
                d[k] = v
            with open(dp, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            print(f"Updated dictionary: {dp} (Now {len(d)} words)")

def update_figure_quotes():
    fig_paths = [
        'data/la_boite_a_merveilles/figures.json',
        '1bac-reader/data/boite/figures.json',
        'data/la_boite_a_merveilles/detected_figures.json',
        '1bac-reader/data/boite/detected_figures.json'
    ]
    for fp in fig_paths:
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                figs = json.load(f)
            for fig in figs:
                q = fig.get('quote', '')
                if q in EXACT_FIGURE_CLAUSE_REPLACEMENTS:
                    fig['quote'] = EXACT_FIGURE_CLAUSE_REPLACEMENTS[q]
                elif len(q) > 120 and ',' in q:
                    # Shorten overly long multi-clause paragraph quotes to target clause
                    clauses = [c.strip() for c in q.split(',') if len(c.strip()) > 15]
                    if len(clauses) >= 2 and fig.get('type') == 'Antithèse':
                        fig['quote'] = f"{clauses[0]}, {clauses[1]}"
            with open(fp, 'w', encoding='utf-8') as f:
                json.dump(figs, f, ensure_ascii=False, indent=2)
            print(f"Updated figure quotes in: {fp}")

def main():
    update_dictionary()
    update_figure_quotes()

if __name__ == '__main__':
    main()
