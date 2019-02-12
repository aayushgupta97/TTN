var p = prompt("Enter the principal amount: ")
var r = prompt("Enter the rate of interest: ")
r = r/100 ; 
var t = prompt("Enter the time: ")

S = p*r*t ; 
alert("The Value of Simple Interest is : " + S) ;

alert("The total amout is: " + (p*(1+r*t))) ;

document.getElementById("si").innerHTML = S ;

