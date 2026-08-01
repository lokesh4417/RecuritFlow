const API_URL = "http://127.0.0.1:5000";

// Upload Resume
const uploadForm = document.getElementById("uploadForm");

if (uploadForm) {
    uploadForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const fileInput = document.getElementById("resume");

        if (fileInput.files.length === 0) {
            alert("Please select a resume.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", fileInput.files[0]);

        try {
            const response = await fetch(API_URL + "/upload", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            if (data.success) {

                localStorage.setItem(
                    "candidate",
                    JSON.stringify(data.candidate)
                );

                localStorage.setItem(
                    "ai",
                    data.ai_analysis
                );

                alert("Resume uploaded successfully!");

                window.location.href = "candidate.html";

            } else {

                alert(data.message);

            }

        } catch (error) {

            console.error(error);
            alert("Cannot connect to backend.");

        }
    });
}