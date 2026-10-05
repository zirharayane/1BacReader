/**
 * 1Bac Reader Smart Tokenizer & Annotation Engine
 * Pure text highlight slicing preserving raw whitespace, punctuation and typography.
 * Completely free of inline badges and emojis.
 */

window.BacParser = (function () {
  'use strict';

  window.BacFiguresRegistry = [];
  window.BacVocabRegistry = [];

  function norm(str) {
    if (!str) return '';
    return str
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/['’\ufffd]/g, "'")
      .trim();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function escapeRegExp(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  /**
   * Normalize and store dictionary & figures registries in memory
   */
  function resetRegistries(dictionary, figures) {
    window.BacFiguresRegistry = Array.isArray(figures) ? [...figures] : [];

    if (Array.isArray(dictionary)) {
      window.BacVocabRegistry = [...dictionary];
    } else if (typeof dictionary === 'object' && dictionary !== null) {
      window.BacVocabRegistry = Object.keys(dictionary).map(wordKey => {
        const val = dictionary[wordKey];
        return {
          word: wordKey,
          type: val.type || 'Vocabulaire',
          definition: val.fr_def || val.definition || '',
          fousha: val.arabic || val.fousha || '',
          darija: val.darija || '',
          english: val.english || '',
          context_note: val.context_note || ''
        };
      });
    } else {
      window.BacVocabRegistry = [];
    }
  }

  /**
   * Bionic Reading text transformer - gently bolds initial syllables without altering spacing
   */
  function applyBionic(text) {
    if (!text) return '';
    return text.replace(/\b([A-Za-zÀ-ÿ0-9]{2,})\b/g, function (match) {
      const splitPoint = Math.ceil(match.length * 0.45);
      const boldPart = match.slice(0, splitPoint);
      const restPart = match.slice(splitPoint);
      return `<strong class="bionic-fixation">${boldPart}</strong>${restPart}`;
    });
  }

  /**
   * Find word intervals respecting French word boundaries and apostrophes
   */
  function findWordIntervals(normRaw, rawWord, vocabIdx) {
    const intervals = [];
    const nWord = norm(rawWord);
    if (!nWord || nWord.length < 2) return intervals;

    // Pattern matching word + optional plural endings (-s, -es, -x) bounded by punctuation/spaces/apostrophe
    const pattern = `(?<=^|[\\s.,;:!?"'’«»\\(\\)\\[\\]\\-])(${escapeRegExp(nWord)}(?:s|es|x)?)(?=$|[\\s.,;:!?"'’«»\\(\\)\\[\\]\\-])`;
    let regex;
    try {
      regex = new RegExp(pattern, 'gi');
    } catch (e) {
      regex = new RegExp(`\\b${escapeRegExp(nWord)}\\b`, 'gi');
    }

    let match;
    while ((match = regex.exec(normRaw)) !== null) {
      intervals.push({
        start: match.index,
        end: match.index + match[0].length,
        type: 'vocab',
        id: vocabIdx,
        priority: 1
      });
    }
    return intervals;
  }

  /**
   * Annotate raw paragraph or dialogue text with pure, badge-free highlights.
   * Keeps raw whitespace and punctuation attached to surrounding characters verbatim.
   */
  function annotateText(rawText, isBionic) {
    if (!rawText) return '';

    const normRaw = norm(rawText);
    const intervals = [];

    // 1. Figures of Style intervals
    window.BacFiguresRegistry.forEach((fig, fIdx) => {
      if (!fig.quote || fig.quote.length < 3) return;
      const nQuote = norm(fig.quote);
      let startPos = 0;
      while ((startPos = normRaw.indexOf(nQuote, startPos)) !== -1) {
        intervals.push({
          start: startPos,
          end: startPos + nQuote.length,
          type: 'figure',
          id: fIdx,
          priority: 2
        });
        startPos += nQuote.length;
      }
    });

    // 2. Vocabulary intervals
    window.BacVocabRegistry.forEach((vItem, vIdx) => {
      const found = findWordIntervals(normRaw, vItem.word, vIdx);
      intervals.push(...found);
    });

    if (intervals.length === 0) {
      const safe = escapeHtml(rawText);
      return isBionic ? applyBionic(safe) : safe;
    }

    // Sort intervals by start index ascending, then longest match first
    intervals.sort((a, b) => {
      if (a.start !== b.start) return a.start - b.start;
      return (b.end - b.start) - (a.end - a.start);
    });

    // Slicing without altering surrounding punctuation or whitespace
    let html = '';
    let curr = 0;

    for (let i = 0; i < intervals.length; i++) {
      const it = intervals[i];
      if (it.start < curr) continue; // Skip overlapping interval

      if (it.start > curr) {
        const slice = escapeHtml(rawText.slice(curr, it.start));
        html += isBionic ? applyBionic(slice) : slice;
      }

      const matchText = rawText.slice(it.start, it.end);
      const safeMatch = escapeHtml(matchText);
      const displayMatch = isBionic ? applyBionic(safeMatch) : safeMatch;

      // Pure highlights without inline badges/emojis
      if (it.type === 'figure') {
        html += `<span class="hl-figure" data-fig-idx="${it.id}">${displayMatch}</span>`;
      } else {
        html += `<span class="hl-vocab" data-vocab-idx="${it.id}">${displayMatch}</span>`;
      }

      curr = it.end;
    }

    if (curr < rawText.length) {
      const tail = escapeHtml(rawText.slice(curr));
      html += isBionic ? applyBionic(tail) : tail;
    }

    return html;
  }

  return {
    norm: norm,
    escapeHtml: escapeHtml,
    resetRegistries: resetRegistries,
    annotateText: annotateText,
    applyBionic: applyBionic
  };
})();
