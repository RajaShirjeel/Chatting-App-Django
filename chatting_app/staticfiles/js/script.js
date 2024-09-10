console.log('hello');
console.log('you');
// const userPk = "{{ user.pk }}"; 
// console.log('userpk', userPk);

// const chatSocket = new WebSocket(
//     'ws://' + window.location.host + '/ws/chat/' + userPk + '/'
// );

// chatSocket.onopen = function(e) {
//     console.log("WebSocket connection opened successfully");
// };

// chatSocket.onerror = function(e) {
//     console.error("WebSocket error", e);
// };

// chatSocket.onmessage = function(e) {
//     const data = JSON.parse(e.data);
//     console.log("Received message:", data.message); // Check if this logs
//     document.querySelector('.chats').innerHTML += '<div class="chat-message chat-other"><p>' + data.message + '</p></div>';
// };

// chatSocket.onclose = function(e) {
//     console.error("Chat socket closed unexpectedly");
// };

// document.querySelector('.send-button').onclick = function(e) {
//     const messageInput = document.querySelector('.message-box');
//     const message = messageInput.value;
//     console.log("Sending message:", message);  // Check if this logs

//     chatSocket.send(JSON.stringify({
//         'message': message
//     }));
//     messageInput.value = '';
// };