document.getElementById('logout_confirm').addEventListener('click', function (event) {
    event.preventDefault();
    if (confirm('Are you sure want to logout ?')) {
        document.getElementById('logoutForm').submit();

    }
})

document.getElementById('logout_confirm2').addEventListener('click', function (event) {
    console.log("hello i am clicked ");
    event.preventDefault();
    if (confirm("Are you sure want to logout ?")) {
        document.getElementById('logoutForm2').submit();
    }
})


document.getElementById('profile-pic-input').addEventListener('change', function (event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
        document.getElementById('profile-pic').style.backgroundImage = 'url(' + e.target.result + ')';
        document.getElementById('profile-pic').textContent = '';
    };
    reader.readAsDataURL(file);
});


