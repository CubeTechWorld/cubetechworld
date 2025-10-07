/*const chatbox = document.getElementById('chatbox');
const chatFloat = document.getElementById('chat-float');
const chatClose = document.getElementById('chatbox-close');
const typingIndicator = document.getElementById('typing-indicator');

chatFloat.addEventListener('click', () => {
  chatbox.style.display = 'flex';
  chatFloat.style.display = 'none';
});

chatClose.addEventListener('click', () => {
  chatbox.style.display = 'none';
  chatFloat.style.display = 'flex';
});

function sendMessage(event) {
  if (event.key === 'Enter') sendChat();
}

function sendButtonMessage() { sendChat(); }

function sendChat() {
  const input = document.getElementById('chat-input');
  const messages = document.getElementById('messages');
  if (input.value.trim() === '') return;

  // User message
  const userMsg = document.createElement('div');
  userMsg.className = 'message';
  userMsg.textContent = input.value;
  messages.appendChild(userMsg);
  input.value = '';
  messages.scrollTop = messages.scrollHeight;

  // Typing indicator
  typingIndicator.style.display = 'block';
  setTimeout(() => {
    typingIndicator.style.display = 'none';
    const botMsg = document.createElement('div');
    botMsg.className = 'message bot';
    botMsg.textContent = "Thanks for your message! We will get back to you soon 😊😊";
    messages.appendChild(botMsg);
    messages.scrollTop = messages.scrollHeight;
  }, 1200);
}*/

