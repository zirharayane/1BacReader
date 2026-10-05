/**
 * 1Bac Reader Dashboard Application Script
 * Controls bookshelf interactions, exam stats overview, and quick chapter launchers.
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  initBookshelfStats();
});

async function initBookshelfStats() {
  const statsMap = {
    boite: { vocab: 0, figures: 0 },
    condamne: { vocab: 0, figures: 0 },
    antigone: { vocab: 0, figures: 0 }
  };

  try {
    const promises = [
      fetch('data/boite/dictionary.json').then(r => r.json()).catch(() => ({})),
      fetch('data/boite/figures.json').then(r => r.json()).catch(() => []),
      fetch('data/condamne/dictionary.json').then(r => r.json()).catch(() => ({})),
      fetch('data/condamne/figures.json').then(r => r.json()).catch(() => []),
      fetch('data/antigone/dictionary.json').then(r => r.json()).catch(() => ({})),
      fetch('data/antigone/figures.json').then(r => r.json()).catch(() => [])
    ];

    const [bDict, bFig, cDict, cFig, aDict, aFig] = await Promise.all(promises);

    const getLen = (d) => Array.isArray(d) ? d.length : (typeof d === 'object' && d !== null ? Object.keys(d).length : 0);

    statsMap.boite.vocab = getLen(bDict);
    statsMap.boite.figures = getLen(bFig);

    statsMap.condamne.vocab = getLen(cDict);
    statsMap.condamne.figures = getLen(cFig);

    statsMap.antigone.vocab = getLen(aDict);
    statsMap.antigone.figures = getLen(aFig);

    updateStatBadges(statsMap);
  } catch (err) {
    console.warn("Could not fetch bookshelf stats:", err);
  }
}

function updateStatBadges(statsMap) {
  Object.keys(statsMap).forEach(key => {
    const cardEl = document.querySelector(`.book-card[data-work="${key}"]`);
    if (cardEl) {
      const vocabEl = cardEl.querySelector('.stat-vocab-count');
      const figEl = cardEl.querySelector('.stat-fig-count');
      if (vocabEl) vocabEl.textContent = `${statsMap[key].vocab} mots explicités`;
      if (figEl) figEl.textContent = `${statsMap[key].figures} figures examens`;
    }
  });
}
