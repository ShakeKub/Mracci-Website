function typeText(element, text, duration) {
    element.classList.add('typing');
    element.textContent = text;

    const delay = duration / text.length;
    let index = 0;
  
    const interval = setInterval(() => {
      element.textContent = text.substring(0, ++index);
      if (index === text.length) {
        clearInterval(interval);
        element.classList.remove('typing');  
      }
    }, delay);
  }
  
  document.addEventListener("DOMContentLoaded", function() {

    const h1 = document.querySelector('#typed-h1');
    const p = document.querySelector('#typed-p');
  
    typeText(h1, 'Welcome to Mráčci', 1500);  
    setTimeout(() => typeText(p, 'Sophisticated Discord bots with many options and features.', 1500), 1600);
  });

document.querySelectorAll('.nav-button').forEach(button => {
    button.addEventListener('click', () => {
      alert(`${button.textContent} button clicked`);
    });
  });
  
  document.querySelector('.login').addEventListener('click', () => {
    alert('Log in clicked');
  });
  
  document.querySelector('.left-icon').addEventListener('click', () => {
    alert('Search icon clicked');
  });
  

  