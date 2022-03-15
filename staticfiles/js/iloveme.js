function toggleProfileIMGSelect() {
    const form = document.getElementById('profile-pic-form');
    if(form.classList.contains('hide')) {
        form.classList.remove('hide');
    } else {
        form.classList.add('hide');
    }
}
function toggleChangePageTitle() {
    const titleTag = document.getElementById('header-title');
    const titleForm = document.getElementById('header-title-form');
    if (titleTag.classList.contains('hide')) {
        titleTag.classList.remove('hide');
        titleForm.classList.add('hide');
    } else {
        titleForm.classList.remove('hide');
        titleTag.classList.add('hide');
    }
}
document.getElementById('add_profile_pic_btn').addEventListener(
    'click',
    toggleProfileIMGSelect
)
document.getElementById('change-page-title-btn').addEventListener(
    'click',
    toggleChangePageTitle
)