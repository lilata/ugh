function checkIfPasswordMatch() {
    const password = document.querySelector('#id_password').value;
    const passwordAgainInput = document.querySelector('#id_password_again');
    const passwordAgain = passwordAgainInput.value;
    const match =  password === passwordAgain;
    if (!match) {
        passwordAgainInput.classList.add('red-border');
    } else {
        passwordAgainInput.classList.remove('red-border');
    }
    return match;
}
function checkIfPasswordGood() {
    const passwordInput = document.querySelector('#id_password');
    const password = passwordInput.value;
    let passwordOK = true;
    const noteTooShortTag = document.querySelector('#note_password_too_short');
    if (password.length < 6) {
        noteTooShortTag.classList.remove('invisible-note');
        passwordOK = false;
    } else {
        noteTooShortTag.classList.add('invisible-note');
    }
    const noteWrongLengthTag = document.querySelector('#note_password_wrong_length');
    if (password.length > 4096) {
        noteWrongLengthTag.classList.remove('invisible-note');
        passwordOK = false;
    } else {
        noteWrongLengthTag.classList.add('invisible-note');
    }
    const noteNoSpecialChar = document.querySelector('#note_password_no_special_char');
    if (!password.match(/[ `~!@#$%^&*()_+{}|?\[\]\/\\.,<>;':"-=]/)) {
        passwordOK = false;
        noteNoSpecialChar.classList.remove('invisible-note');
    } else {
        noteNoSpecialChar.classList.add('invisible-note');
    }
    if (!passwordOK) {
        passwordInput.classList.add('red-border');
    } else {
        passwordInput.classList.remove('red-border');
    }
    return passwordOK;
}
async function checkUsernameFromAPI (username) {
    if (username.length === 0) {
        return {message: false};
    }
    const resp = await fetch(userExistAPI, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify({'username': username})
    });
    return resp.json();
}
function checkIfUsernameIsUsed() {
    const usernameInput = document.querySelector('#id_username');
    const username = usernameInput.value;
    checkUsernameFromAPI(username).then(data => {
        const usernameUsed = data['message'];
        const noteTag = document.querySelector('#note_username_used');
        if (usernameUsed) {
            noteTag.classList.remove('invisible-note');
            usernameInput.classList.add('red-border');
        } else {
            noteTag.classList.add('invisible-note');
            usernameInput.classList.remove('red-border');
        }
    });
}
function checkUsernameLength() {
    const usernameInput = document.querySelector('#id_username');
    const usernameLen = usernameInput.value.length;
    const goodLength = usernameLen > 0 && usernameLen < 256;
    const noteTag = document.querySelector('#note_username_wrong_length');
    if (!goodLength) {
        noteTag.classList.remove('invisible-note');
        usernameInput.classList.add('red-border');
    } else {
        noteTag.classList.add('invisible-note');
        usernameInput.classList.remove('red-border');
    }
    return goodLength;
}
function register(e) {
    e.preventDefault();

    const registrationForm = document.querySelector('#registration_form');
    const username = document.querySelector('#id_username').value;
    if (username.length === 0) {
        return
    }
    if (checkIfCaptchaInputted() &&
        checkIfPasswordGood() &&
        checkIfPasswordMatch() &&
        checkUsernameLength()
        ) {
        checkUsernameFromAPI(username).then(data => {
            if (!data['message']) {
                registrationForm.submit();
            }
        });
    }
}
window.onload = () => {
    checkIfUsernameIsUsed();
    getCaptcha();
    document.querySelector("#id_username").addEventListener(
        'keyup',
        checkUsernameLength
    );
    document.querySelector('#captcha_img').addEventListener(
        'click',
        getCaptcha
    );
    document.querySelector("#id_password_again").addEventListener(
        'keyup',
        checkIfPasswordMatch
    );
    document.querySelector("#id_password").addEventListener(
        'keyup',
        checkIfPasswordMatch
    );
    document.querySelector("#id_password").addEventListener(
        'keyup',
        checkIfPasswordGood
    );
    document.querySelector('#id_username').addEventListener(
        'blur',
        checkIfUsernameIsUsed
    );
    document.querySelector('#id_register_button').addEventListener(
        'click',
        register
    );
}