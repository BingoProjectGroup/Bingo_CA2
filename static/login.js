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


  