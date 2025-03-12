const socket = new WebSocket("wss://echo.websocket.org");

// Connection opened
socket.addEventListener("open", () => {
  console.log("WebSocket is open now.");
  socket.send("Hello WebSocket!");
});

// Listen for messages
socket.addEventListener("message", event => {
  console.log("Message from server:", event.data);
});

// Connection closed
socket.addEventListener("close", () => {
  console.log("WebSocket is closed now.");
});
