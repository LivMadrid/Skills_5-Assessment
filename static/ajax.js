// Replace this with your code
//add an event listener to form
const form = getElementById('form');

form.addEventListener('submit', (evt) => {
  console.log(evt);
});

$.get('/api/human/<int:human_id>', (response) => {
  $('/api/human/<int:human_id>').value(response);
});