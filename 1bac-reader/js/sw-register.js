/**
 * Service Worker Registration & Offline Toast Notification
 */

if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    navigator.serviceWorker.register('./sw.js')
      .then(function (registration) {
        console.log('1Bac Reader SW registered with scope:', registration.scope);
        showOfflineToast('Mode Hors-Ligne Prêt ⚡ (Toutes les œuvres sont enregistrées)');
      })
      .catch(function (err) {
        console.warn('1Bac Reader SW registration failed:', err);
      });
  });
}

function showOfflineToast(msg) {
  const toast = document.getElementById('offlineToast');
  if (toast) {
    toast.querySelector('.toast-msg').textContent = msg;
    toast.classList.add('visible');
    setTimeout(() => {
      toast.classList.remove('visible');
    }, 4000);
  }
}
