$(document).ready(function() {
// question 1
console.log("Hello World!") ; 
// question 2
$('#test').addClass('load')
// question 3
$('[class$=new]').css('color', 'red') ; 
// question 4
$('#q4').attr('disabled', true)
// question 5
$('#main > .target').css('font-size','100px')
// question 6
$("#q6").replaceWith("<p>" + $("#q6").html())
// question 7 and question 8
$(".clickme").on('click', function(e){
	$("#clickit").clone().insertAfter("#clickit").on('click', e.handleObj.handler);
}) 
// question 9
$('#q9').on('change',(e) => {
	$('#text-select').html($(e.target).val())

})

// question 10
 $('#hover-text').mouseover((e) => {
        $(e.target).next().toggle()
})

// question 11
$("a").click(function(e){
        e.preventDefault();
      });
// question 12
  $('#parent-click').on('click', (e) => {
        alert('You clicked on the parent!')
    })
    $('#child-click').on('click', (e) => {
        e.stopPropagation()
})
// question 13



    // $(".clickPrevent").click(function(){
    //     $(".l1").hide();
    //   });
    //   $(".clickPrevent .l1").click(function(e){
    //     e.stopPropagation();
    //   });


// question 14
$( ".buttonColor" ).click(function() {
        $( "td" ).each(function( index, element ) {
          // element == this
          var value1 = Number($( this ).html());
          if (value1 > 10) {
            $( element ).css( "backgroundColor", "yellow" );  
          }
        });
      });
// question 15

//  $.ajax({
//         url: 'https://aayushgupta97.github.io/TTN/databases/exercise3',
//         success: (res) => {
//             //console.log(res)
//             $('#ajax-res').html('An ajax request was successful, its result is in the console.')
//         }
// });

// question 16
// $('.cross-button').on('click', (e) => {
//         $.ajax({
//             url: 'https://yamalik42.github.io/TTN-html-css/vc-exercise.txt',
//             success: (res) => {
//                 $(e.target).parent().remove()
//             }
//         })
// })

// question 17
var width = 720;
    var animationSpeed = 2000;
    var pause = 500;
    var currentSlide = 1;

    var $slider = $('#slider');
    var $slideContainer = $('.slides', $slider);
    var $slides = $('.slide', $slider);

    var interval;

    function startSlider() {
        interval = setInterval(function() {
            $slideContainer.animate({'margin-left': '-='+width}, animationSpeed, function() {
                if (++currentSlide === $slides.length) {
                    currentSlide = 1;
                    $slideContainer.css('margin-left', 0);
                }
            });
        }, pause);
    }
    function pauseSlider() {
        clearInterval(interval);
    }

    $slideContainer
        .on('mouseenter', pauseSlider)
        .on('mouseleave', startSlider);

    startSlider();


})