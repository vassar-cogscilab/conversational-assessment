// Wait for the entire webpage to load before running any code
document.addEventListener('DOMContentLoaded', () => {
    
    // Find the elements on the page
    const chatInput = document.querySelector('.input-wrapper input');
    const sendButton = document.querySelector('.send-btn');
    const chatMessages = document.getElementById('chatMessages');

    // Check if the elements exist (helps with debugging)
    if (!chatInput || !sendButton || !chatMessages) {
        console.error("Error: Could not find chat elements. Check your HTML classes.");
        return;
    }

    // Function to add a new message bubble to the screen
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        
        messageDiv.innerHTML = `
            <div class="message-content">
                <p>${text}</p>
            </div>
        `;
        
        chatMessages.appendChild(messageDiv);
        
        // Automatically scroll down to show the new message
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to handle sending the message
    function handleSendMessage() {
        const userText = chatInput.value.trim();
        
        // Stop if the input is completely empty
        if (!userText) return;
        
        // 1. Show the user's message
        addMessage(userText, 'user');
        chatInput.value = ''; // Clear the input box
        
        // 2. Show a temporary "thinking" message from the AI
        setTimeout(() => {
            addMessage("I am processing your request...", "ai");
        }, 1000);
    }

    // Run the function when clicking the Send button
    sendButton.addEventListener('click', handleSendMessage);

    // Run the function when pressing the Enter key inside the input box
    chatInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevents accidental page reloads
            handleSendMessage();
        }
    });
});
