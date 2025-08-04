// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatMessages = document.getElementById("chat-messages");

    chatForm.addEventListener("submit", function(e) {
        e.preventDefault();

        const message = userInput.value.trim();
        if (!message) return;

        // Display user message
        addMessage(message, "user");
        userInput.value = "";

        // Get CSRF token
        const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

        // Get chatbot response
        fetch("/get-response/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "X-CSRFToken": csrftoken
            },
            body: `user_input=${encodeURIComponent(message)}`
        })
        .then(response => response.json())
        .then(data => {
            addMessage(data.response, "bot");
        })
        .catch(error => {
            console.error("Error:", error);
            addMessage("Sorry, an error occurred.", "bot");
        });
    });

    function addMessage(message, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.textContent = message;
        messageDiv.className = sender === "user" ? "user-message" : "bot-message";
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
})