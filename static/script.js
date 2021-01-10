let userprofile = document.querySelectorAll('#userprofile');
userprofile.forEach(el => {
    el.addEventListener('click', function() {
        console.log('a');
        a = el.querySelector('#detail');
        a.classList.toggle('userprofile_show');

    });

})
