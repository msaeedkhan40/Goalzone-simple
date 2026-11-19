/** teams.js – fetch and render team cards */
document.addEventListener('DOMContentLoaded', async () => {
  showLoading('teams-container');
  try {
    const { teams } = await fetchAPI('/api/teams');
    const container = document.getElementById('teams-container');
    if (!teams.length) {
      container.innerHTML = `<div class="empty-state"><div class="empty-icon">🏆</div><p>No teams found.</p></div>`;
      return;
    }
    container.innerHTML = `<div class="teams-grid">${teams.map(teamCard).join('')}</div>`;
    setTimeout(initScrollAnimations, 60);
  } catch (e) {
    showError('teams-container', 'Could not load teams. Is the Flask server running?');
  }
});

function teamCard(t) {
  const logo = t.logo
    ? `<img class="team-card-logo" src="${t.logo}" alt="${t.name}" onerror="this.outerHTML='<div class=team-logo-ph>🏆</div>'">`
    : `<div class="team-logo-ph">🏆</div>`;
  return `
  <div class="team-card fade-up">
    ${logo}
    <div class="team-name">${t.name}</div>
    <div class="team-country">🌍 ${t.country}</div>
    <div class="team-meta">
      <span>📅 Est. ${t.founded}</span>
      <span>🏟️ ${t.stadium}</span>
    </div>
    <p class="team-desc">${t.description}</p>
  </div>`;
}
