$(document).ready(function() {
// question 1
console.log("Hello World!") ; 
// question 2
$('#test').addClass('load')
// question 3
$('[class$=new]').css('color', 'red') ; 
// question 4
$(':submit').attr('disabled', true)
// question 5
$('#main > .target').css('font-size','100px')
// question 6
$("#q6").replaceWith("<p>" + $("#q6").html())
// question 7
$(".clickme").on('click', function(e){
	$("#clickit").clone().insertAfter("#clickit").on('click', e.handleObj.handler);
}) 
// question 8
// question 9
// question 10
// question 11
// question 12
// question 13
// question 14
// question 15
// question 16
// question 17
})