# 1BacReader

> **Notice**: This project was an experiment and was considered a failure / abandoned by its creator. If anyone wants this code, feel free to take it, use it, modify it, or build something better with it.

---

## Overview

An offline-first reading web application and NLP ingestion pipeline tailored for Moroccan 1ère Année Baccalauréat (1Bac) students studying the three prescribed French literary works:

1. **La Boîte à Merveilles** — Ahmed Sefrioui
2. **Le Dernier Jour d'un Condamné** — Victor Hugo
3. **Antigone** — Jean Anouilh

---

## Features

- **PWA Reader (`1bac-reader/`)**:
  - Dual-mode reading interface: Flip-book spread (PageFlip) and continuous scroll.
  - Trilingual vocabulary popups (French definition, Modern Standard Arabic الفصحى, Moroccan Darija الدارجة, English).
  - 10-year regional exam figures of style annotations with frequency statistics and analytical justifications.
  - ADHD reading support tools (Bionic Reading fixation, reading ruler, line spotlight, font scaling, night/sepia/cream themes).
- **Data & NLP Pipeline (`pipeline/`)**:
  - Chapter & scene segmentation extractors (`extract_boite.py`, `extract_hugo.py`, `extract_antigone.py`).
  - Automated figures of style pattern matchers & 10-year regional exam frequency analyzer.
  - Dictionary generation with contextual Darija translations.

---

## Project Structure

```
├── 1bac-reader/               # Frontend web app (Vanilla JS / CSS / HTML)
│   ├── css/                  # Reader & portal styling
│   ├── js/                   # Parser, reader controller, inspector drawer
│   ├── data/                 # Normalized JSON datasets for the 3 works
│   ├── index.html            # Main bookshelf & reader portal
│   └── sw.js                 # Offline service worker
├── data/                     # Raw & processed book corpora
├── pipeline/                 # Python NLP ingestion & analysis scripts
├── tests/                    # Pytest suite
└── REGIONAL_EXAM_FIGURES_GUIDE.md # Reference guide for regional exam figures
```

---

## Quick Start

### Running the Web Reader Locally
```bash
cd 1bac-reader
# Or run from the project root:
python -m http.server 8080
```
Open `http://localhost:8080/1bac-reader/` in your browser.

### Running Pipeline Tests
```bash
pytest tests/test_pipeline.py -v
```

---

## License

Unlicense / Public Domain / MIT — Take whatever you need.
