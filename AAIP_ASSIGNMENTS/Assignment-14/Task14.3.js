// JavaScript to validate a simple login form (non-empty username/password)

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    let errorMsg = document.getElementById('loginError');
    if (!errorMsg) {
        errorMsg = document.createElement('div');
        errorMsg.id = 'loginError';
        errorMsg.style.color = 'red';
        errorMsg.style.marginBottom = '8px';
        form.prepend(errorMsg);
    }

    form.addEventListener('submit', function (event) {
        errorMsg.textContent = '';

        const errors = [];
        if (!usernameInput.value.trim()) errors.push('Username is required.');
        if (!passwordInput.value.trim()) errors.push('Password is required.');

        if (errors.length > 0) {
            event.preventDefault();
            errorMsg.textContent = errors.join(' ');
        }
    });

    [usernameInput, passwordInput].forEach(input => {
        input.addEventListener('input', () => {
            errorMsg.textContent = '';
        });
    });
});
