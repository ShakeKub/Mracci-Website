async function checkConnection() {
    try {
        let response = await fetch('/check_connection');
        let data = await response.json();
        let statusMessage = document.getElementById('status-message');
        if (data.connected) {
            statusMessage.textContent = "Your bot is connected!";
        } else {
            statusMessage.textContent = "Your bot is not connected.";
        }
    } catch (error) {
        console.error('Error checking connection:', error);
    }
}

window.onload = checkConnection;