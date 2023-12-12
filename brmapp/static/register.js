document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('form');
    const username = document.getElementById('id_username');
    const email = document.getElementById('id_email');
    const password = document.getElementById('id_password1');
    const confirmPassword = document.getElementById('id_password2');


    function showError(input, message) {
        const wrapper = input.closest('.input-box');
        const small = wrapper.querySelector('small');
        wrapper.className = 'input-box error';
        small.innerText = message;
    }


    function showSuccess(input) {
        const wrapper = input.closest('.input-box');
        wrapper.className = 'input-box success';
    }


    form.addEventListener('submit', function (e) {
        e.preventDefault();

        let isFormValid = true;

        if (username.value.trim() === '') {
            showError(username, 'Username is required');
            isFormValid = false;
        } else {
            showSuccess(username);
        }

        if (email.value.trim() === '') {
            showError(email, 'Email is required');
            isFormValid = false;
        } else if (!isValidEmail(email.value)) {
            showError(email, 'Email is not valid');
            isFormValid = false;
        } else {
            showSuccess(email);
        }

        if (password.value.trim() === '') {
            showError(password, 'Password is required.');
            isFormValid = false;
        } else if (password.value.length < 8) {
            showError(password, 'Password must be at least 8 characters long.');
            isFormValid = false;
        } else {
            showSuccess(password);
        }

        if (confirmPassword.value.trim() === '') {
            showError(confirmPassword, 'Confirm password is required.');
            isFormValid = false;
        } else if (password.value !== confirmPassword.value) {
            showError(confirmPassword, 'Passwords do not match.');
            isFormValid = false;
        } else {
            showSuccess(confirmPassword);
        }

        if (isFormValid) {

            alert('Form submitted successfully!');
        } else {

            alert('Form submission failed. Please check the errors and try again.');
        }
    });

    function isValidEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
});
