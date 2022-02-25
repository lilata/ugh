async function getCaptcha() {
    const captchaTokenFieldTag = document.querySelector('#captcha_token');
    let body = {};
    if (captchaTokenFieldTag.value.length !== 0) {
        body = {previous_token: captchaTokenFieldTag.value};
    }
    const captchaImageTag = document.querySelector('#captcha_img');
    captchaImageTag.src = '';
    captchaImageTag.alt = 'captcha is loading...';
    captchaTokenFieldTag.value = '';
    const resp = await fetch(newCaptchaAPI, {
        method: 'POST',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(body)
    });
    resp.json().then(data => {
        captchaImageTag.src = data['url'];
        captchaImageTag.alt = 'captcha';
        captchaTokenFieldTag.value = data['token'];
    })
}
function checkIfCaptchaInputted() {
    const captchaTag = document.querySelector('#id_captcha');
        const inputted = captchaTag.value.length !== 0;
    if (!inputted) {
        captchaTag.classList.add('red-border');
    } else {
        captchaTag.classList.remove('red-border');
    }
    return inputted;
}