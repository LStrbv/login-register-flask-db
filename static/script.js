let userprofile = document.querySelectorAll('#userprofile');
userprofile.forEach(el => {
    el.addEventListener('mouseover', function() {
        el
        .querySelector('#detail')
        .classList.toggle('userprofile_show');

    });

    el.addEventListener('mouseout', function() {
        el
        .querySelector('#detail')
        .classList.remove('userprofile_show');

    });

})


