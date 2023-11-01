document.addEventListener('DOMContentLoaded', function () {
  // Fetch the translation data from the URL
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Extract the translation of "hello" from the data
      const helloTranslation = data.hello;
      // Display the translation in the div#hello
      document.getElementById('hello').textContent = helloTranslation;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
