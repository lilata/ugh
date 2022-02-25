function getNextUrl() {
    const params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });
    if (params.next) {
        document.querySelector('#id_next').value = params.next;
    }
}
function checkInputted(selector) {
    return () => {
        const tag = document.querySelector(selector);
        const inputted = tag.value.length !== 0;
        if (!inputted) {
            tag.classList.add('red-border');
        } else {
            tag.classList.remove('red-border');
        }
        return inputted;
    }
}
function login(e) {
    e.preventDefault();
    let canLogin = true
    for (s of ['#id_username', '#id_password', '#id_captcha']) {
        if (!checkInputted(s)()) {
            canLogin = false;
            break;
        }
    }
    if (canLogin) {
        const loginForm = document.querySelector('#login-form');
        loginForm.submit();
    }

}
window.onload = () => {
    getNextUrl();
    getCaptcha();
    document.querySelector('#captcha_img').addEventListener(
        'click',
        getCaptcha
    );
    document.querySelector('#id_username').addEventListener(
        'keyup',
        checkInputted('#id_username')
    );
    document.querySelector('#id_password').addEventListener(
        'keyup',
        checkInputted('#id_password')
    );
    document.querySelector('#id_login_button').addEventListener(
        'click',
        login
    )
}