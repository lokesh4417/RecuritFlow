const API_URL = "http://127.0.0.1:5000";

let skillsChart = null;
let candidateChart = null;

// ==============================
// Load Dashboard
// ==============================
async function loadDashboard() {

    try {

        const response = await fetch(API_URL + "/candidates");

        if (!response.ok) {
            throw new Error("Failed to fetch candidates");
        }

        const candidates = await response.json();

        // Dashboard Cards
        document.getElementById("candidateCount").textContent = candidates.length;
        document.getElementById("resumeCount").textContent = candidates.length;

        // Candidate Table
        const table = document.getElementById("candidateTable");
        table.innerHTML = "";

        if (candidates.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="3" class="text-center">
                        No Candidates Found
                    </td>
                </tr>
            `;

            return;
        }

        candidates.forEach(candidate => {

            table.innerHTML += `
<tr>
    <td>${candidate.name}</td>
    <td>${candidate.email}</td>
    <td>${candidate.skills}</td>

    <td>

        <button
            class="btn btn-primary btn-sm"
            onclick='viewCandidate(${JSON.stringify(candidate)})'>

            View

        </button>

    </td>

</tr>
`;

        });

        // Build Charts
        createCharts(candidates);

    }

    catch (error) {

        console.error(error);

        alert("Unable to connect to backend.");

    }

}

// ==============================
// Search
// ==============================
function searchCandidates() {

    const keyword = document
        .getElementById("searchBox")
        .value
        .toLowerCase();

    const rows = document.querySelectorAll("#candidateTable tr");

    rows.forEach(row => {

        const text = row.innerText.toLowerCase();

        if (text.includes(keyword)) {

            row.style.display = "";

        } else {

            row.style.display = "none";

        }

    });

}

// ==============================
// Charts
// ==============================
function createCharts(candidates) {

    const skillCounts = {};

    candidates.forEach(candidate => {

        if (candidate.skills) {

            candidate.skills.split(",").forEach(skill => {

                skill = skill.trim();

                skillCounts[skill] = (skillCounts[skill] || 0) + 1;

            });

        }

    });

    // Destroy old charts
    if (skillsChart) {
        skillsChart.destroy();
    }

    if (candidateChart) {
        candidateChart.destroy();
    }

    // Skills Pie Chart
    skillsChart = new Chart(
        document.getElementById("skillsChart"),
        {
            type: "pie",
            data: {
                labels: Object.keys(skillCounts),
                datasets: [{
                    label: "Skills",
                    data: Object.values(skillCounts)
                }]
            }
        }
    );

    // Candidate Count Bar Chart
    candidateChart = new Chart(
        document.getElementById("candidateChart"),
        {
            type: "bar",
            data: {
                labels: ["Candidates"],
                datasets: [{
                    label: "Total Candidates",
                    data: [candidates.length]
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        }
    );

}

// ==============================
// Page Load
// ==============================
window.onload = loadDashboard;
function viewCandidate(candidate){

    localStorage.setItem(
        "candidate",
        JSON.stringify(candidate)
    );

    window.location.href="candidate.html";

}