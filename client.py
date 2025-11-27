html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
</head>
<body>

<h1>WebSocket Chat</h1>

<form onsubmit="sendMessage(event)">
    <input type="text" id="messageText" autocomplete="off" />
    <button>Send</button>
</form>

<ul id="messages"></ul>

<script>
    // Connect WebSocket
    var ws = new WebSocket("ws://localhost:8000/ws/chat");

    // When message comes from server
    ws.onmessage = function(event) {
        var list = document.getElementById("messages");
        var item = document.createElement("li");
        item.textContent = event.data;
        list.appendChild(item);
    };

    // Send message
    function sendMessage(event) {
        var input = document.getElementById("messageText");
        ws.send(input.value);
        input.value = "";
        event.preventDefault();
    }
</script>

</body>
</html>
"""
