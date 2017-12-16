
//Function for GPA Calculations
/*
Needs:
  - Implementation to remove Course
  - Check if user entered correct information
*/
(function(){

  //Cloned element of grade options
  var optionClone = $('#grade-options').clone();

  //Add Course
  $("#add-course").on('click', function(){
    optionClone.clone().appendTo($('.inner-box'))
  })

  //Calculate GPA
  //Needs to check if user has actually put in data
  $("#calculate-gpa").on('click', function(){
    alert('wtf');
    var gradeList = $('.inner-box').find('form');
    var qualityPoints = 0.00;
    var creditHours = 0;
    for (var i = 0; i < gradeList.length; i++){
      //debugger;
      qualityPoints += parseInt(gradeList[i][1].value) * parseFloat(gradeList[i][2].value);
      creditHours += parseInt(gradeList[i][1].value);
    }
    $('#gpa').html((qualityPoints/creditHours).toFixed(2))
  })

})()
