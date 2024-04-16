const commands = {
    1: 'ls', 
    2: 'emulationstation', // retropi
    3: 'hypnotix', //iptv
    4: 'scrcpy --video-codec=h265 -m1920 --max-fps=60', //scrcpy
    5: 'TradingView' // Stocks
};

function runCommand(index) {
    eel.spawn_shell(commands[index])().then(output => {
        document.getElementById('output').innerText = output;
    });
}

// Wasd navigation
var buttons = Array.from(document.querySelectorAll('button'));
        var currentButtonIndex = 0;
        buttons[currentButtonIndex].focus();

        document.addEventListener('keydown', function(event) {
            switch (event.key) {
                case 'w':
                    if (currentButtonIndex - 4 >= 0) {
                        currentButtonIndex -= 4;
                    }
                    break;
                case 's':
                    if (currentButtonIndex + 4 < buttons.length) {
                        currentButtonIndex += 4;
                    }
                    break;
                case 'a':
                    if (currentButtonIndex - 1 >= 0) {
                        currentButtonIndex -= 1;
                    }
                    break;
                case 'd':
                    if (currentButtonIndex + 1 < buttons.length) {
                        currentButtonIndex += 1;
                    }
                    break;
                case ' ':
                    buttons[currentButtonIndex].click();
                    break;
            }
            buttons[currentButtonIndex].focus();
        }
        );

eel.get_system_info()(function(system_info) {
    document.getElementById('platform').textContent = 'Platform: ' + system_info.platform;
    document.getElementById('release').textContent = 'Release: ' + system_info.release;
    document.getElementById('machine').textContent = 'Machine: ' + system_info.machine;
    document.getElementById('total-ram').textContent = 'Total RAM: ' + system_info.total_ram + ' GB';
    document.getElementById('used-ram').textContent = 'Used RAM: ' + system_info.used_ram + ' GB';
    document.getElementById('ram-percentage').textContent = 'RAM Usage: ' + system_info.ram_percentage + '%';
});

// Call getSystemInfo immediately and then every 1000 milliseconds
getSystemInfo();
setInterval(getSystemInfo, 1000);

function updateTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const ampm = hours >= 12 ? 'pm' : 'am';
    const day = now.getDate();
    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const month = monthNames[now.getMonth()];

    let suffix;
    if (day > 3 && day < 21) suffix = 'th';
    else suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th'][day % 10];

    const strTime = ((hours % 12) || 12) + ':' + (minutes < 10 ? "0" : "") + minutes + ' ' + ampm + ' ' + ' ' + day + suffix + ' ' + month;
    document.getElementById('timeDate').innerText = strTime;
}

setInterval(updateTime, 1000);
updateTime();

function bounce() {
    let ball = document.querySelector(".cssBall");
    ball.style.transition = "0.5s";
    ball.style.width = "55px";
  
    ball.style.bottom = "-151px";
    setTimeout(() => {
      ball.style.bottom = "0px";
      ball.style.transition = "0.7s";
      ball.style.width = "50px";
    }, 450);
  }
  
setInterval(bounce, 1000);