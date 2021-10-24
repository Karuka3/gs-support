/*
document.querySelector('input[type="date"]').addEventListener('change', event => {
    const target = event.target;
    target.setAttribute('data-date', target.value);
}, false);
*/

document.addEventListener('click', function () {
    function dateChanged(e) {
        const target = e.target;
        target.setAttribute('data-date', target.value);
    }

    const date = document.getElementsByClassName('pingdate');
    for (let i = 0; i < date.length; i++) {
        date[i].addEventListener('change', dateChanged, false);
    }

}, false);