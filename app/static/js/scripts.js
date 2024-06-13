// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (username && password) {
                alert('Login successful');
            } else {
                alert('Please fill out all fields');
            }
        });
    }

    const scheduleForm = document.getElementById('scheduleForm');
    if (scheduleForm) {
        scheduleForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const date = document.getElementById('date').value;
            const time = document.getElementById('time').value;
            if (date && time) {
                alert('Schedule submitted successfully');
            } else {
                alert('Please fill out all fields');
            }
        });
    }
});
