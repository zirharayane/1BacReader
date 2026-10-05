/**
 * 1Bac Reader Unified Application Engine
 * Apple Books / Kindle-grade Digital Reader with Academic Highlights & Pure Typography.
 */

(function () {
  'use strict';

  const WORK_CONFIGS = {
    boite: {
      key: 'boite',
      title: "La Boîte à Merveilles",
      author: "Ahmed Sefrioui",
      genre: "Roman Autobiographique",
      dataPath: "data/boite/",
      type: "prose"
    },
    condamne: {
      key: 'condamne',
      title: "Le Dernier Jour d'un Condamné",
      author: "Victor Hugo",
      genre: "Roman à Thèse",
      dataPath: "data/condamne/",
      type: "prose"
    },
    antigone: {
      key: 'antigone',
      title: "Antigone",
      author: "Jean Anouilh",
      genre: "Tragédie Moderne",
      dataPath: "data/antigone/",
      type: "theatre"
    }
  };

  let currentWork = WORK_CONFIGS.boite;
  let pageFlipInstance = null;

  let textData = null;
  let dictionaryData = [];
  let figuresData = [];
  let detectedFiguresData = [];

  let normalizedChapters = []; // [{ title, paragraphs: [] }]
  let normalizedDialogues = []; // [{ speaker, stage_direction, text }]
  let chapterPageMap = [];

  // ADHD & View State
  let currentMode = 'book'; // 'book' or 'scroll'
  let isBionic = false;
  let isSpotlight = false;
  let isRuler = false;
  let currentFontSize = 1.05; // rem

  document.addEventListener('DOMContentLoaded', initApp);

  function initApp() {
    BacInspector.init();
    setupGlobalEventListeners();
    setupADHDTools();

    const params = new URLSearchParams(window.location.search);
    const workParam = params.get('work');

    if (workParam && WORK_CONFIGS[workParam]) {
      window.openWork(workParam);
    } else {
      window.returnToShelf();
    }
  }

  // --- Unified SPA View Switchers ---
  window.openWork = async function (workKey) {
    if (!WORK_CONFIGS[workKey]) return;
    currentWork = WORK_CONFIGS[workKey];

    document.getElementById('viewBookshelf').style.display = 'none';
    document.getElementById('viewReader').style.display = 'flex';

    document.getElementById('readerBookTitle').textContent = currentWork.title;

    await loadWorkData();
    renderCurrentWork();
  };

  window.returnToShelf = function () {
    if (pageFlipInstance) {
      try { pageFlipInstance.destroy(); } catch (e) {}
      pageFlipInstance = null;
    }
    document.getElementById('viewReader').style.display = 'none';
    document.getElementById('viewBookshelf').style.display = 'block';
    window.history.replaceState({}, '', window.location.pathname);
  };

  // --- Data Loading & Normalization ---
  async function loadWorkData() {
    const path = currentWork.dataPath;

    try {
      const [textRes, dictRes, figRes, detFigRes] = await Promise.all([
        fetch(path + (currentWork.type === 'theatre' ? 'scenes.json' : 'chapters.json')),
        fetch(path + 'dictionary.json').catch(() => ({ json: () => ({}) })),
        fetch(path + 'figures.json').catch(() => ({ json: () => [] })),
        fetch(path + 'detected_figures.json').catch(() => ({ json: () => [] }))
      ]);

      textData = await textRes.json();
      dictionaryData = await dictRes.json();
      figuresData = await figRes.json();
      detectedFiguresData = await detFigRes.json();

      normalizedChapters = [];
      normalizedDialogues = [];

      if (currentWork.type === 'prose') {
        if (Array.isArray(textData)) {
          normalizedChapters = textData.map((c, i) => ({
            title: c.chapter_title || `Chapitre ${i + 1}`,
            paragraphs: c.paragraphs || []
          }));
        } else if (typeof textData === 'object' && textData !== null) {
          const keys = Object.keys(textData).sort((a, b) => {
            const numA = parseInt(a.replace(/\D/g, ''), 10) || 0;
            const numB = parseInt(b.replace(/\D/g, ''), 10) || 0;
            return numA - numB;
          });

          normalizedChapters = keys.map(k => {
            const num = parseInt(k.replace(/\D/g, ''), 10) || 1;
            const val = textData[k];
            const paras = Array.isArray(val) ? val : (val.paragraphs || []);
            return {
              title: `Chapitre ${num}`,
              paragraphs: paras
            };
          });
        }
      } else {
        normalizedDialogues = Array.isArray(textData) ? textData : (textData.dialogues || []);
      }

      const combinedFigures = [...figuresData, ...detectedFiguresData];
      BacParser.resetRegistries(dictionaryData, combinedFigures);

    } catch (err) {
      console.error("Error loading work data:", err);
      alert("Erreur lors du chargement des données.");
    }
  }

  // --- Rendering Functions ---
  function renderCurrentWork() {
    buildChapterDropdown();
    buildScrollReader();
    buildEditorialFlipbook();
  }

  function buildChapterDropdown() {
    const select = document.getElementById('selectChapter');
    if (!select) return;
    select.innerHTML = '';

    if (currentWork.type === 'prose') {
      normalizedChapters.forEach((ch, idx) => {
        const opt = document.createElement('option');
        opt.value = idx;
        opt.textContent = ch.title;
        select.appendChild(opt);
      });
    } else {
      const opt = document.createElement('option');
      opt.value = 0;
      opt.textContent = "Texte Intégral - Prologue & Scènes";
      select.appendChild(opt);
    }
  }

  // Build Continuous Scroll View
  function buildScrollReader() {
    const container = document.getElementById('scrollReaderContent');
    if (!container) return;
    container.innerHTML = '';

    if (currentWork.type === 'prose') {
      normalizedChapters.forEach((ch, cIdx) => {
        const section = document.createElement('section');
        section.id = `scrollChapter_${cIdx}`;
        section.innerHTML = `<h2 class="scroll-chapter-heading">${BacParser.escapeHtml(ch.title)}</h2>`;

        ch.paragraphs.forEach(p => {
          const annotated = BacParser.annotateText(p, isBionic);
          section.innerHTML += `<p>${annotated}</p>`;
        });

        container.appendChild(section);
      });
    } else {
      const section = document.createElement('section');
      section.innerHTML = `<h2 class="scroll-chapter-heading">Antigone - Texte Intégral</h2>`;

      normalizedDialogues.forEach(d => {
        const speaker = d.speaker ? d.speaker.trim() : '';
        const direction = d.stage_direction ? d.stage_direction.trim() : '';
        const annotatedText = BacParser.annotateText(d.text || '', isBionic);

        let dHtml = `<div class="dialogue-item">`;
        if (speaker) dHtml += `<span class="speaker-name">${BacParser.escapeHtml(speaker)}</span>`;
        if (direction) dHtml += `<span class="stage-direction">(${BacParser.escapeHtml(direction)})</span>`;
        dHtml += `<p>${annotatedText}</p></div>`;

        section.innerHTML += dHtml;
      });

      container.appendChild(section);
    }
  }

  // Build Editorial Book Spread
  function buildEditorialFlipbook() {
    const container = document.getElementById('flipbookContainer');
    if (!container) return;

    if (pageFlipInstance) {
      try { pageFlipInstance.destroy(); } catch (e) {}
      pageFlipInstance = null;
    }

    container.innerHTML = '';
    chapterPageMap = [];

    const pageElements = [];

    // Left Page: Title & Pédagogie
    const introPage = document.createElement('div');
    introPage.className = 'page';
    introPage.innerHTML = `
      <div class="page-header">
        <span>Édition Pédagogique 1Bac</span>
        <span>Régional Maroc</span>
      </div>
      <div class="page-content">
        <div class="title-page-card">
          <span class="title-page-genre">${BacParser.escapeHtml(currentWork.genre || 'Texte Intégral')}</span>
          <h1 class="title-page-main-title">${BacParser.escapeHtml(currentWork.title)}</h1>
          <p class="title-page-author">${BacParser.escapeHtml(currentWork.author)}</p>
          <div class="title-page-divider"></div>
          <p class="title-page-desc">
            Module d'étude annoté pour l'examen régional : vocabulaire avec traduction en <strong>الدارجة المغربية</strong> et <strong>الفصحى</strong>, et repérage contextuel des <strong>Figures de Style</strong>.
          </p>
        </div>
      </div>
      <div class="page-footer">1</div>
    `;
    pageElements.push(introPage);

    let virtualPage = 2;

    if (currentWork.type === 'prose') {
      normalizedChapters.forEach((ch, cIdx) => {
        chapterPageMap.push({ title: ch.title, pageIndex: virtualPage - 1, chapterIndex: cIdx });

        let currentChunk = [];
        let currentWordCount = 0;

        ch.paragraphs.forEach(pText => {
          const annotated = BacParser.annotateText(pText, isBionic);
          const wCount = pText.split(/\s+/).length;

          if (currentWordCount + wCount > 185 && currentChunk.length > 0) {
            pageElements.push(createPageElement(ch.title, currentChunk, virtualPage));
            virtualPage++;
            currentChunk = [];
            currentWordCount = 0;
          }

          currentChunk.push(annotated);
          currentWordCount += wCount;
        });

        if (currentChunk.length > 0) {
          pageElements.push(createPageElement(ch.title, currentChunk, virtualPage));
          virtualPage++;
        }
      });
    } else {
      chapterPageMap.push({ title: "Antigone", pageIndex: 1, chapterIndex: 0 });

      let currentChunk = [];
      let currentItemCount = 0;

      normalizedDialogues.forEach(d => {
        const speaker = d.speaker ? d.speaker.trim() : '';
        const direction = d.stage_direction ? d.stage_direction.trim() : '';
        const annotatedText = BacParser.annotateText(d.text || '', isBionic);

        let dHtml = `<div class="dialogue-item">`;
        if (speaker) dHtml += `<span class="speaker-name">${BacParser.escapeHtml(speaker)}</span>`;
        if (direction) dHtml += `<span class="stage-direction">(${BacParser.escapeHtml(direction)})</span>`;
        dHtml += `<p>${annotatedText}</p></div>`;

        currentChunk.push(dHtml);
        currentItemCount++;

        if (currentItemCount >= 3) {
          pageElements.push(createPageElement("Antigone - Scène", currentChunk, virtualPage));
          virtualPage++;
          currentChunk = [];
          currentItemCount = 0;
        }
      });

      if (currentChunk.length > 0) {
        pageElements.push(createPageElement("Antigone - Scène", currentChunk, virtualPage));
        virtualPage++;
      }
    }

    if (pageElements.length % 2 !== 0) {
      const blankPage = document.createElement('div');
      blankPage.className = 'page';
      blankPage.innerHTML = `
        <div class="page-header"><span>Notes Personnelles</span><span>1Bac Maroc</span></div>
        <div class="page-content" style="display:flex; justify-content:center; align-items:center; opacity:0.3; font-style:italic;">Fin de l'œuvre</div>
        <div class="page-footer">${virtualPage}</div>
      `;
      pageElements.push(blankPage);
    }

    pageElements.forEach(p => container.appendChild(p));

    if (window.St && window.St.PageFlip) {
      pageFlipInstance = new window.St.PageFlip(container, {
        width: 540,
        height: 700,
        size: "stretch",
        minWidth: 340,
        maxWidth: 620,
        minHeight: 460,
        maxHeight: 820,
        maxShadowOpacity: 0.2,
        showCover: false,
        mobileScrollSupport: true,
        usePortrait: true,
        clickEventForward: true,
        disableFlipByClick: false
      });

      const pages = container.querySelectorAll('.page');
      pageFlipInstance.loadFromHTML(pages);

      pageFlipInstance.on('flip', (e) => {
        updatePageTracker(e.data);
      });

      updatePageTracker(0);
    }
  }

  function createPageElement(title, htmlArray, pageNum) {
    const pageEl = document.createElement('div');
    pageEl.className = 'page';
    pageEl.innerHTML = `
      <div class="page-header">
        <span>${BacParser.escapeHtml(title)}</span>
        <span>1Bac Maroc</span>
      </div>
      <div class="page-content" style="font-size: ${currentFontSize}rem;">
        ${htmlArray.map(item => item.startsWith('<div') ? item : `<p>${item}</p>`).join('')}
      </div>
      <div class="page-footer">${pageNum}</div>
    `;
    return pageEl;
  }

  function updatePageTracker(pageIndex) {
    const total = pageFlipInstance ? pageFlipInstance.getPageCount() : 0;
    const current = pageIndex + 1;

    const display = document.getElementById('pageNumDisplay');
    if (display) display.textContent = `${current} / ${total}`;

    const slider = document.getElementById('pageSlider');
    if (slider) {
      slider.max = Math.max(0, total - 1);
      slider.value = pageIndex;
    }

    if (chapterPageMap.length > 0) {
      const select = document.getElementById('selectChapter');
      if (select) {
        for (let i = chapterPageMap.length - 1; i >= 0; i--) {
          if (pageIndex >= chapterPageMap[i].pageIndex) {
            select.value = chapterPageMap[i].chapterIndex;
            break;
          }
        }
      }
    }
  }

  window.flipNextPage = function () {
    if (pageFlipInstance) pageFlipInstance.flipNext();
  };

  window.flipPrevPage = function () {
    if (pageFlipInstance) pageFlipInstance.flipPrev();
  };

  // --- Controls & ADHD Tools ---
  function setupGlobalEventListeners() {
    const btnNext = document.getElementById('btnNextPage');
    const btnPrev = document.getElementById('btnPrevPage');
    if (btnNext) btnNext.addEventListener('click', window.flipNextPage);
    if (btnPrev) btnPrev.addEventListener('click', window.flipPrevPage);

    const slider = document.getElementById('pageSlider');
    if (slider) {
      slider.addEventListener('input', function () {
        if (pageFlipInstance) pageFlipInstance.flip(parseInt(this.value, 10));
      });
    }

    const chapterSelect = document.getElementById('selectChapter');
    if (chapterSelect) {
      chapterSelect.addEventListener('change', function () {
        const cIdx = parseInt(this.value, 10);
        if (currentMode === 'book') {
          const match = chapterPageMap.find(item => item.chapterIndex === cIdx);
          if (match && pageFlipInstance) {
            pageFlipInstance.flip(match.pageIndex);
          }
        } else {
          const section = document.getElementById(`scrollChapter_${cIdx}`);
          if (section) section.scrollIntoView({ behavior: 'smooth' });
        }
      });
    }

    const themeButtons = document.querySelectorAll('.theme-btn');
    themeButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        const theme = this.getAttribute('data-theme');
        document.body.className = `theme-${theme}`;
        themeButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
      if (currentMode === 'book') {
        if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
          window.flipNextPage();
        } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
          window.flipPrevPage();
        }
      }
    });

    const btnModeBook = document.getElementById('btnModeBook');
    const btnModeScroll = document.getElementById('btnModeScroll');

    if (btnModeBook && btnModeScroll) {
      btnModeBook.addEventListener('click', () => switchViewMode('book'));
      btnModeScroll.addEventListener('click', () => switchViewMode('scroll'));
    }
  }

  function switchViewMode(mode) {
    currentMode = mode;
    const bookStage = document.getElementById('book3DWrapper');
    const scrollReader = document.getElementById('scrollReaderWrapper');
    const bottomToolbar = document.getElementById('readerToolbar');
    const btnModeBook = document.getElementById('btnModeBook');
    const btnModeScroll = document.getElementById('btnModeScroll');

    if (mode === 'book') {
      bookStage.style.display = 'flex';
      scrollReader.classList.remove('active');
      if (bottomToolbar) bottomToolbar.style.display = 'flex';
      btnModeBook.classList.add('active');
      btnModeScroll.classList.remove('active');
    } else {
      bookStage.style.display = 'none';
      scrollReader.classList.add('active');
      if (bottomToolbar) bottomToolbar.style.display = 'none';
      btnModeScroll.classList.add('active');
      btnModeBook.classList.remove('active');
    }
  }

  function setupADHDTools() {
    const btnBionic = document.getElementById('btnToolBionic');
    if (btnBionic) {
      btnBionic.addEventListener('click', function () {
        isBionic = !isBionic;
        this.classList.toggle('active', isBionic);
        renderCurrentWork();
      });
    }

    const btnRuler = document.getElementById('btnToolRuler');
    const rulerEl = document.getElementById('readingRuler');

    if (btnRuler && rulerEl) {
      btnRuler.addEventListener('click', function () {
        isRuler = !isRuler;
        this.classList.toggle('active', isRuler);
        rulerEl.classList.toggle('active', isRuler);
      });

      window.addEventListener('mousemove', function (e) {
        if (isRuler && rulerEl) {
          rulerEl.style.top = `${e.clientY - 22}px`;
        }
      });
    }

    const btnSpotlight = document.getElementById('btnToolSpotlight');
    if (btnSpotlight) {
      btnSpotlight.addEventListener('click', function () {
        isSpotlight = !isSpotlight;
        this.classList.toggle('active', isSpotlight);
        document.body.classList.toggle('spotlight-active', isSpotlight);
      });
    }

    const btnFontMinus = document.getElementById('btnFontMinus');
    const btnFontPlus = document.getElementById('btnFontPlus');

    if (btnFontMinus) {
      btnFontMinus.addEventListener('click', () => {
        if (currentFontSize > 0.9) {
          currentFontSize = Math.max(0.9, currentFontSize - 0.05);
          applyFontSize();
        }
      });
    }

    if (btnFontPlus) {
      btnFontPlus.addEventListener('click', () => {
        if (currentFontSize < 1.35) {
          currentFontSize = Math.min(1.35, currentFontSize + 0.05);
          applyFontSize();
        }
      });
    }
  }

  function applyFontSize() {
    document.querySelectorAll('.page-content').forEach(el => {
      el.style.fontSize = `${currentFontSize}rem`;
    });
    const scrollContent = document.querySelector('.scroll-reader-content');
    if (scrollContent) {
      scrollContent.style.fontSize = `${currentFontSize + 0.05}rem`;
    }
  }

})();
