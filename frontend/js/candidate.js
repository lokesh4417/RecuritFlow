// =========================================
// RecruitFlow Candidate Profile
// =========================================

const candidate = JSON.parse(localStorage.getItem("candidate"));
const aiAnalysis = localStorage.getItem("ai");


console.log("Candidate Data:", candidate);
console.log("AI Analysis:", aiAnalysis);


if (!candidate) {

    document.body.innerHTML = `
        <div class="container mt-5">
            <div class="alert alert-danger">
                <h3>No Candidate Selected</h3>
                <a href="upload.html" class="btn btn-primary mt-3">
                    Upload Resume
                </a>
            </div>
        </div>
    `;

}
else {


    // =========================
    // Candidate Information
    // =========================

    document.getElementById("name").textContent =
        candidate.name || "Not Available";


    document.getElementById("email").textContent =
        candidate.email || "Not Available";


    document.getElementById("phone").textContent =
        candidate.phone || "Not Available";


    // =========================
    // Skills
    // =========================

    const skillsList = document.getElementById("skills");

    skillsList.innerHTML = "";


    if (candidate.skills) {

        candidate.skills.split(",").forEach(skill => {

            skillsList.innerHTML += `
                <li class="list-group-item">
                    ${skill.trim()}
                </li>
            `;

        });

    }
    else {

        skillsList.innerHTML = `
            <li class="list-group-item">
                No Skills Found
            </li>
        `;

    }



    // =========================
    // AI Analysis Display
    // =========================

    if(aiAnalysis){

        document.getElementById("analysis").textContent =
            aiAnalysis;


        // Resume Score
        const scoreMatch =
        aiAnalysis.match(/Resume Score:\s*([^\n]+)/i);

        if(scoreMatch){

            document.getElementById("score").textContent =
            scoreMatch[1].trim();

        }



        // Recommended Role

        const roleMatch =
        aiAnalysis.match(/Recommended Job Role:\s*([^\n]+)/i);

        if(roleMatch){

            document.getElementById("role").textContent =
            roleMatch[1].trim();

        }



        // Experience Level

        const experienceMatch =
        aiAnalysis.match(/Experience Level:\s*([^\n]+)/i);

        if(experienceMatch){

            document.getElementById("experience").textContent =
            experienceMatch[1].trim();

        }



        // Hiring Recommendation

        const hiringMatch =
        aiAnalysis.match(/Hiring Recommendation:\s*([^\n]+)/i);

        if(hiringMatch){

            document.getElementById("hiring").textContent =
            hiringMatch[1].trim();

        }


    }

    else{

        document.getElementById("analysis").textContent =
        "AI Analysis not available.";

    }

}