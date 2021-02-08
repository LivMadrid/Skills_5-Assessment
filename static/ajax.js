'use strict';

$('#submit').on('click'), () => {
  $.get('/api/human/<int:human_id>', {'human_id': human.human_id}, (res) => {
    $('#fname').html(res);
  });



  //// HELP! Feel like I am digging myself into a deeper hole of confusion. I am not sure where I am going wrong here.
//Tried different ways of adding event listener, GET reqeusts, and reviewed all notes and demos and I am still confused on how to write this. 
//Am I on the right track?. I know I am probably making this more complicated than is. 

// I understand how it is supposed to work - once user clicks submit - event listener calls function to refresh page with appropriate coresponding
//data to human_id number and update "display human " section from "unknown" to fname, lname, email...
// Is there something different when a parameter def get_human(human_id) is passed through? 



  // $('fname').load('/api/human/<int:human_id>')


// $('#get-human').on('submit', (evt) => {
//   evt.preventDefault();
 
// const form = getElementById('form');
//   form.addEventListener('submit', (evt) => {
//   console.log(evt); 
 
// const DisplayData = {
//   fname: $('#fname-field').val(),
//   lname: $('#lname-field').val(),
//   email: $('#email-field').val()
// };
 


  //   $('#human-id').value(res);
  // }); 
  
// $.get('/api/human/<int:human_id>', DisplayData, (res) => {
//   $('#human-id').value(res);
// }); 




// I don't really understand why this is not working..... 

// // Replace this with your code
// //add an event listener to form
// function submitSelect(evt)
//   evt.preventDefault();
  
// const form = getElementById('form');
// form.addEventListener('submit', (evt) => {
//   console.log(evt);
// });

// const DisplayData = {
//   fname: $('#fname-field').val(),
//   lname: $('#lname-field').val(),
//   email: $('#email-field').val()
// };

// $('#get-human').on('submit', submitSelect);

// $.get('/api/human/<int:human_id>', DisplayData, (response) => {
//   $('/api/human/<int:human_id>').value(response);
// });
