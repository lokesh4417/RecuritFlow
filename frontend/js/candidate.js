// =========================================
// RecruitFlow Candidate Profile
// =========================================

const candidate = JSON.parse(localStorage.getItem("candidate"));
const aiAnalysis = localStorage.getItem("ai");

if (!candidate) {

    document.body.innerHTML = `
        <div class="container mt-5">
            <div class="alert alert-danger">
                <h3>No Candidate Selected</h3>
                <a href="dashboard.html" class="btn btn-primary mt-3">
                    Go to Dashboard
                </a>
            </div>
        </div>
    `;

}
else {

    // Candidate Information
    document.getElementById("name").textContent =
        candidate.name || "Not Available";

    document.getElementById("email").textContent =
        candidate.email || "Not Available";

    document.getElementById("phone").textContent =
        candidate.phone || "Not Available";

    // Skills
    const skills = document.getElementById("skills");
    skills.innerHTML = "";

    if (candidate.skills) {

        candidate.skills.split(",").forEach(skill => {

            skills.innerHTML += `
                <li class="list-group-item">
                    ${skill.trim()}
                </li>
            `;

        });

    } else {

        skills.innerHTML = `
            <li class="list-group-item">
                No Skills Found
            </li>
        `;

    }

    // AI Analysis
    document.getElementById("analysis").textContent =
    aiAnalysis || "AI Analysis not available.";

// Extract Resume Score
const scoreMatch = aiAnalysis?.match(/Resume Score:\s*(.*)/i);
if (scoreMatch) {
    document.getElementById("score").textContent =
        scoreMatch[1].trim();
}

// Extract Recommended Role
const roleMatch = aiAnalysis?.match(/Recommended Job Role:\s*(.*)/i);
if (roleMatch) {
    document.getElementById("role").textContent =
        roleMatch[1].trim();
}

// Extract Experience Level
const expMatch = aiAnalysis?.match(/Experience Level:\s*(.*)/i);
if (expMatch) {
    document.getElementById("experience").textContent =
        expMatch[1].trim();
}

// Extract Hiring Recommendation
const hireMatch = aiAnalysis?.match(/Hiring Recommendation:\s*(.*)/i);
if (hireMatch) {
    document.getElementById("hiring").textContent =
        hireMatch[1].trim();
}
}