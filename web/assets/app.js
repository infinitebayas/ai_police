const profileSelect = document.getElementById('profile');
const form = document.getElementById('assessment-form');
const statusNode = document.getElementById('status');
const outputNode = document.getElementById('output');
const basePath = document.body.dataset.basePath || '';

function apiUrl(path) {
  return `${basePath}${path}`;
}

async function loadProfiles() {
  const response = await fetch(apiUrl('/profiles'));
  const data = await response.json();
  profileSelect.innerHTML = '';
  data.profiles.forEach((profile) => {
    const option = document.createElement('option');
    option.value = profile.id;
    option.textContent = profile.name;
    profileSelect.appendChild(option);
  });
  statusNode.textContent = 'Profiles loaded. Ready for assessment.';
}

function getCasePayload() {
  return {
    jurisdiction: document.getElementById('jurisdiction').value,
    summary: document.getElementById('summary').value,
    involves_child: document.getElementById('involves_child').checked,
    involves_woman: document.getElementById('involves_woman').checked,
    imminent_threat: document.getElementById('imminent_threat').checked,
    exploitation_indicator: document.getElementById('exploitation_indicator').checked,
    cyberbullying_indicator: document.getElementById('cyberbullying_indicator').checked,
    harassment_indicator: document.getElementById('harassment_indicator').checked,
    crisis_context: document.getElementById('crisis_context').checked,
    evidence_available: false,
    requested_by_public_nodal_support: document.getElementById('requested_by_public_nodal_support').checked,
    tags: [],
  };
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  statusNode.textContent = 'Generating recommendation...';
  outputNode.textContent = '{}';

  const payload = {
    profile_name: profileSelect.value,
    case: getCasePayload(),
  };

  try {
    const apiResponse = await fetch(apiUrl('/recommend'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (!apiResponse.ok) {
      throw new Error(`Request failed with status ${apiResponse.status}`);
    }

    const data = await apiResponse.json();
    outputNode.textContent = JSON.stringify(data, null, 2);
    statusNode.textContent = 'Recommendation ready.';
  } catch (error) {
    statusNode.textContent = 'Unable to generate recommendation.';
    outputNode.textContent = JSON.stringify({ error: String(error) }, null, 2);
  }
});

async function init() {
  try {
    await loadProfiles();
  } catch (error) {
    statusNode.textContent = 'Unable to load profiles.';
    outputNode.textContent = JSON.stringify({ error: String(error) }, null, 2);
  }
}

await init();
