window.onload = checkConnection;

function showPanel(panel) {
    // Hide all panel content
    const panels = document.querySelectorAll('.panel-content');
    panels.forEach(panel => panel.classList.remove('active'));

    // Show the selected panel
    const activePanel = document.getElementById(`${panel}-content`);
    activePanel.classList.add('active');
}


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

