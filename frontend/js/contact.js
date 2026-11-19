/** contact.js – handle contact form submission */
document.addEventListener('DOMContentLoaded', () => {
  const form    = document.getElementById('contact-form');
  const btn     = document.getElementById('submit-btn');
  const success = document.getElementById('alert-success');
  const error   = document.getElementById('alert-error');
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name    = document.getElementById('name').value.trim();
    const email   = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !email || !message) {
      showAlert(error, '⚠️ Please fill in all three fields.');
      return;
    }

    btn.disabled = true;
    btn.textContent = 'Sending…';
    hideAlerts();

    try {
      const res  = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, message }),
      });
      const data = await res.json();
      if (res.ok) {
        showAlert(success, `✅ ${data.message}`);
        form.reset();
      } else {
        showAlert(error, `❌ ${data.error || 'Something went wrong.'}`);
      }
    } catch (err) {
      showAlert(error, '❌ Cannot reach the server. Make sure Flask is running.');
    } finally {
      btn.disabled = false;
      btn.textContent = 'Send Message ✉️';
    }
  });

  function showAlert(el, msg) {
    hideAlerts();
    el.textContent = msg;
    el.classList.add('show');
    el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  function hideAlerts() {
    success.classList.remove('show');
    error.classList.remove('show');
  }
});
