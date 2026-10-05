/**
 * 1Bac Reader Inspector Module
 * Safe in-memory lookup for definitions, Darija/Fousha translations, and figures of style.
 */

window.BacInspector = (function () {
  'use strict';

  let drawerEl = null;
  let drawerBodyEl = null;
  let closeBtnEl = null;

  function init() {
    drawerEl = document.getElementById('inspectorDrawer');
    drawerBodyEl = document.getElementById('inspectorBody');
    closeBtnEl = document.getElementById('btnCloseDrawer');

    if (closeBtnEl) {
      closeBtnEl.addEventListener('click', close);
    }

    // Delegated click handler for highlight badges
    document.addEventListener('click', function (e) {
      const vocabEl = e.target.closest('.hl-vocab');
      const figEl = e.target.closest('.hl-figure');

      if (vocabEl) {
        e.stopPropagation();
        const vIdx = vocabEl.getAttribute('data-vocab-idx');
        if (vIdx !== null && window.BacVocabRegistry[vIdx]) {
          showVocab(window.BacVocabRegistry[vIdx]);
        }
      } else if (figEl) {
        e.stopPropagation();
        const fIdx = figEl.getAttribute('data-fig-idx');
        if (fIdx !== null && window.BacFiguresRegistry[fIdx]) {
          showFigure(window.BacFiguresRegistry[fIdx]);
        }
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawerEl && drawerEl.classList.contains('open')) {
        close();
      }
    });
  }

  function open() {
    if (drawerEl) {
      drawerEl.classList.add('open');
      const bookContainer = document.querySelector('.reader-stage-container');
      if (bookContainer) bookContainer.classList.add('drawer-docked');
    }
  }

  function close() {
    if (drawerEl) {
      drawerEl.classList.remove('open');
      const bookContainer = document.querySelector('.reader-stage-container');
      if (bookContainer) bookContainer.classList.remove('drawer-docked');
    }
  }

  function showVocab(entry) {
    if (!entry) return;

    let html = `
      <div class="annotation-card">
        <div class="annotation-target">📖 ${escapeHtml(entry.word)}</div>
        
        <div class="field-group">
          <span class="field-label">Définition (Français)</span>
          <div class="field-value">${escapeHtml(entry.definition || entry.def_fr || 'Terme spécifique du programme 1Bac.')}</div>
        </div>

        ${entry.fousha || entry.def_ar ? `
        <div class="field-group">
          <span class="field-label">اللغة العربية الفصحى</span>
          <div class="field-value-arabic">${escapeHtml(entry.fousha || entry.def_ar)}</div>
        </div>
        ` : ''}

        ${entry.darija ? `
        <div class="field-group">
          <span class="field-label">الدارجة المغربية (الشرح البسيط)</span>
          <div class="field-value-darija">${escapeHtml(entry.darija)}</div>
        </div>
        ` : ''}

        ${entry.context_note ? `
        <div class="field-group">
          <span class="field-label">Note Contextuelle</span>
          <div class="field-value" style="font-size:0.85rem; color:#94a3b8;">${escapeHtml(entry.context_note)}</div>
        </div>
        ` : ''}
      </div>
    `;

    drawerBodyEl.innerHTML = html;
    open();
  }

  function showFigure(entry) {
    if (!entry) return;

    let html = `
      <div class="annotation-card">
        <div class="annotation-target">✨ ${escapeHtml(entry.type || 'Figure de Style')}</div>

        <div class="field-group">
          <span class="field-label">Citation du Texte</span>
          <div class="field-value figure-quote-box">
            « ${escapeHtml(entry.quote)} »
          </div>
        </div>

        <div class="field-group">
          <span class="field-label">Explication & Effet Littéraire</span>
          <div class="field-value">${escapeHtml(entry.explanation || entry.effect || "Procédé de style récurrent dans les épreuves régionales.")}</div>
        </div>

        ${entry.exam_frequency || entry.rank ? `
        <div class="exam-frequency-badge">
          🔥 Examen Régional: ${escapeHtml(entry.exam_frequency || `Figure N°${entry.rank} des annales`)}
        </div>
        ` : ''}
      </div>
    `;

    drawerBodyEl.innerHTML = html;
    open();
  }

  function escapeHtml(str) {
    return BacParser.escapeHtml(str);
  }

  return {
    init: init,
    open: open,
    close: close,
    showVocab: showVocab,
    showFigure: showFigure
  };
})();
