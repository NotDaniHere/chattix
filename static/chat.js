const chatbox = document.getElementById("chatbox");
const chatForm = document.getElementById("chatForm");

async function fetchMessages() {
    try {
        const response = await fetch('/receive');
        const messages = await response.json();
        chatbox.innerHTML = messages.map(msg => `
            <div>
                <span class="username">${msg.username}</span>: 
                <span>${msg.message}</span>
                <small>[${msg.timestamp}]</small>
            </div>
        `).join("");
        chatbox.scrollTop = chatbox.scrollHeight;
    } catch (err) {
        console.error("Error fetching messages:", err);
    }
}

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const message = document.getElementById("message").value;

    try {
        await fetch('/send', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, message }),
        });
        document.getElementById("message").value = "";
        fetchMessages();
    } catch (err) {
        console.error("Error sending message:", err);
    }
});

setInterval(fetchMessages, 2000); // Refresh messages every 2 seconds
fetchMessages(); // Initial fetch
