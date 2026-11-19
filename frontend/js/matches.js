/** matches.js – fetch and render match cards */
document.addEventListener('DOMContentLoaded', async () => {
  showLoading('matches-container');
  try {
    const { matches } = await fetchAPI('/api/matches');
    const container = document.getElementById('matches-container');
    if (!matches.length) {
      container.innerHTML = `<div class="empty-state"><div class="empty-icon">📅</div><p>No matches right now.</p></div>`;
      return;
    }
    container.innerHTML = `<div class="matches-grid">${matches.map(matchCard).join('')}</div>`;
    setTimeout(initScrollAnimations, 60);
  } catch (e) {
    showError('matches-container', 'Could not load matches. Is the Flask server running?');
  }
});

function matchCard(m) {
  const hLogo = m.home_logo ? `<img class="team-logo" src="${m.home_logo}" alt="${m.home_team}" onerror="this.replaceWith(ph())">` : ph();
  const aLogo = m.away_logo ? `<img class="team-logo" src="${m.away_logo}" alt="${m.away_team}" onerror="this.replaceWith(ph())">` : ph();
  function ph() { const d = document.createElement('div'); d.className='logo-placeholder'; d.textContent='⚽'; return d; }
  const hL = m.home_logo ? `<img class="team-logo" src="${m.home_logo}" alt="${m.home_team}" onerror="this.outerHTML='<div class=logo-placeholder>⚽</div>'">` : `<div class="logo-placeholder">⚽</div>`;
  const aL = m.away_logo ? `<img class="team-logo" src="${m.away_logo}" alt="${m.away_team}" onerror="this.outerHTML='<div class=logo-placeholder>⚽</div>'">` : `<div class="logo-placeholder">⚽</div>`;
  return `
  <div class="match-card fade-up">
    <div class="match-card-top">
      <span class="badge badge-green">${m.competition}</span>
      <span class="match-comp-label">${formatDate(m.date)} · ${m.time}</span>
    </div>
    <div class="match-teams">
      <div class="match-team">${hL}<span class="team-name-sm">${m.home_team}</span></div>
      <div class="match-score"><span class="score-val">${m.home_score} – ${m.away_score}</span><span class="score-vs">VS</span></div>
      <div class="match-team">${aL}<span class="team-name-sm">${m.away_team}</span></div>
    </div>
    <div class="match-footer">
      <span>🏟️ ${m.venue}</span>
      <span class="badge badge-green">⏰ Upcoming</span>
    </div>
  </div>`;
}
