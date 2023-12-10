function validateEmail() {
    var emailInput = document.getElementsByName('email')[0];
    var emailError = document.getElementById('emailError');
  
    
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var email = emailInput.value.trim();
  
    if (!emailRegex.test(email)) {
      emailError.textContent = 'Invalid email format';
      return false;
    } else {
      emailError.textContent = '';
      return true;
    }
  }
  // Prevent form submission if email is invalid
  document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
      if (!validateEmail()) {
        event.preventDefault(); 
      }
    });
  });

  function submitLoginForm() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Make a POST request to the Flask backend
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirect or perform other actions on successful login
            alert(data.message);
        } else {
            // Display error message
            document.getElementById('error-message').textContent = data.message;
        }
    })
    .catch(error => console.error('Error:', error));
}