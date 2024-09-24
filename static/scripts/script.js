// Модальные окна для авторизации
function openLoginModal() {
    document.getElementById('authModal').style.display = 'block';
}

function openRegistrationModal() {
    document.getElementById('registerModal').style.display = 'block';
}

function closeModals() {
    document.getElementById('authModal').style.display = 'none';
    document.getElementById('registerModal').style.display = 'none';
}

// Закрытие модальных окон при нажатии за пределами окна
window.onclick = function(event) {
    const loginModal = document.getElementById('login-modal');
    const regModal = document.getElementById('registration-modal');
    if (event.target === loginModal) {
        loginModal.style.display = 'none';
    }
    if (event.target === regModal) {
        regModal.style.display = 'none';
    }
}

// Функция регистрации
function registerUser() {
    const nickname = document.getElementById("registerNickname").value;
    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;

    const data = { nickname, email, password };

    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Регистрация прошла успешно!');
            closeModal('registerModal');
            updateHeaderAfterAuth(data.user); // Функция для обновления шапки после входа
        } else {
            alert('Ошибка регистрации: ' + data.message);
        }
    });
}

// Функция авторизации
function authenticateUser() {
    const email = document.getElementById("authEmail").value;
    const password = document.getElementById("authPassword").value;

    const data = { email, password };

    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Вход успешен!');
            closeModal('authModal');
            updateHeaderAfterAuth(data.user);
        } else {
            alert('Ошибка входа: ' + data.message);
        }
    });
}

// Функция обновления шапки после входа
function updateHeaderAfterAuth(user) {
    const loginButton = document.getElementById("loginButton");
    const registerButton = document.getElementById("registerButton");

    loginButton.style.display = 'none';
    registerButton.style.display = 'none';

    const profileButton = document.createElement('button');
    profileButton.innerText = `Профиль (${user.nickname})`;
    profileButton.onclick = () => window.location.href = 'profile.html';

    const balanceButton = document.createElement('button');
    balanceButton.innerText = `Баланс: ${user.balance} Р`;

    document.querySelector('header').appendChild(profileButton);
    document.querySelector('header').appendChild(balanceButton);
}


// Переход на страницу лота
function openLot(lotId) {
    window.location.href = `/lotInfo?id=${lotId}`;
}
