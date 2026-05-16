const socket = io();

function sendMessage() {

    let username =
        document.getElementById("username").value;

    let message =
        document.getElementById("message").value;

    if(username === "" || message === "") {
        return;
    }

    socket.emit("send_message", {

        username: username,
        message: message
    });

    document.getElementById("message").value = "";
}

socket.on("message", function(data) {

    let messages =
        document.getElementById("messages");

    let div =
        document.createElement("div");

    div.classList.add("msg");

    div.innerHTML = `
        <strong>${data.username}</strong>
        <p>${data.message}</p>
    `;

    messages.appendChild(div);

    messages.scrollTop =
        messages.scrollHeight;
});