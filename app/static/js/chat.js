document.addEventListener('DOMContentLoaded', function() {
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const chatContainer = document.getElementById('chat-container');
    const topicId = chatContainer.dataset.topicId;
    const loadingIndicator = document.createElement('div');
    loadingIndicator.className = 'loading-indicator';
    loadingIndicator.innerHTML = '<svg class="animate-spin h-5 w-5 text-gray-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>';

    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function addMessage(content, isUser = true) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'assistant-message'}`;
        messageDiv.innerHTML = content;
        chatContainer.appendChild(messageDiv);
        scrollToBottom();
    }

    messageForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message
        addMessage(message);
        messageInput.value = '';

        // Show loading indicator
        chatContainer.appendChild(loadingIndicator);
        scrollToBottom();

        try {
            const response = await fetch('/chat/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    topic_id: topicId,
                    message: message
                })
            });

            const data = await response.json();
            
            // Remove loading indicator
            loadingIndicator.remove();

            if (data.status === 'success') {
                addMessage(data.response, false);
                initializeCodeBlocks();
            } else {
                throw new Error(data.error || 'Unknown error');
            }
        } catch (error) {
            loadingIndicator.remove();
            addMessage('Error: ' + error.message, false);
        }
    });

    // Initial scroll to bottom
    scrollToBottom();
});