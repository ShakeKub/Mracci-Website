function checkConnection() {
    fetch('/check_connection')
        .then(response => response.json())
        .then(data => {
            const statusMessage = document.getElementById('status-message');
            if (data.connected) {
                statusMessage.textContent = "You are connected to your Discord bot.";
                statusMessage.style.color = "green";
            } else {
                statusMessage.textContent = "You need to link your Discord bot to access this page.";
                statusMessage.style.color = "red";
                setTimeout(() => {
                    window.location.href = '/';  // Redirect to home page
                }, 5000); // Redirect after 5 seconds
            }
        })
        .catch(error => {
            console.error('Error checking connection:', error);
        });
}

setInterval(checkConnection, 10000);

checkConnection();