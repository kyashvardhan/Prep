const socket = new WebSocket("wss://your-websocket-server.com");

document.getElementById("comment-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const comment = document.getElementById("comment-input").value;
    socket.send(JSON.stringify({ comment }));
    document.getElementById("comment-input").value = "";
});

socket.addEventListener("message", function(event) {
    const commentData = JSON.parse(event.data);
    const commentList = document.getElementById("comment-list");
    const newComment = document.createElement("li");
    newComment.textContent = commentData.comment;
    commentList.appendChild(newComment);
});
