/** news.js – fetch and render news cards */
document.addEventListener('DOMContentLoaded', async () => {
  showLoading('news-container');
  try {
    const { news } = await fetchAPI('/api/news');
    const container = document.getElementById('news-container');
    if (!news.length) {
      container.innerHTML = `<div class="empty-state"><div class="empty-icon">📰</div><p>No articles found.</p></div>`;
      return;
    }
    container.innerHTML = `<div class="news-grid">${news.map(newsCard).join('')}</div>`;
    setTimeout(initScrollAnimations, 60);
  } catch (e) {
    showError('news-container', 'Could not load news. Is the Flask server running?');
  }
});

const catBadge = {
  'Analysis':'badge-blue','Preview':'badge-gold',
  'Champions League':'badge-purple','Features':'badge-green','Tactics':'badge-blue'
};

function newsCard(a) {
  const bc = catBadge[a.category] || 'badge-green';
  const initials = a.author.split(' ').map(w => w[0]).join('');
  const fallback = 'https://images.unsplash.com/photo-1508098682722-e99c43a406b2?w=800&q=80';
  return `
  <div class="news-card fade-up">
    <div class="news-img-wrap">
      <img src="${a.image}" alt="${a.title}" loading="lazy" onerror="this.src='${fallback}'">
      <div class="news-img-overlay"></div>
      <div class="news-cat-badge"><span class="badge ${bc}">${a.category}</span></div>
    </div>
    <div class="news-body">
      <h3 class="news-title">${a.title}</h3>
      <p class="news-desc">${a.description}</p>
      <div class="news-meta">
        <div class="news-author">
          <div class="author-av">${initials}</div>
          <span>${a.author}</span>
        </div>
        <span>${formatDate(a.date)}</span>
      </div>
    </div>
  </div>`;
}
