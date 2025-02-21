document.addEventListener("DOMContentLoaded", function () {
    const checkSpamButton = document.getElementById("checkSpamButton");
    const emailInput = document.getElementById("text");

    if (!checkSpamButton || !emailInput) {
        console.error("Error: Button or input field not found! Check HTML IDs.");
        return;
    }

    checkSpamButton.addEventListener("click", function () {
        const emailText = emailInput.value.trim();

        if (!emailText) {
            showError("Please enter an email before checking.");
            return;
        }

        console.log(" Sending request to backend...");
        
        fetch("http://127.0.0.1:5000/classify", {
            method: "POST",
            mode: "cors",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email_text: emailText })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Server responded with status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Response received:", data);
            showResult(data.prediction);
        })
        .catch(error => {
            console.error(" Error:", error);
            showError("Error connecting to the server. Make sure the backend is running.");
        });
    });
});

function showResult(prediction) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = `Prediction: <strong>${prediction}</strong>`;
    resultDiv.style.color = "green";
    resultDiv.style.display = "block";
}

function showError(message) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = message;
    resultDiv.style.color = "red";
    resultDiv.style.display = "block";
}
