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

let addBtn = document.querySelectorAll('#add_friend');
console.log(addBtn);
let count = 0;
function clickFunction() {
  count+=1;
  document.getElementById("count").innerHTML = count;
}
addBtn.forEach(el => 'click', clickFunction());