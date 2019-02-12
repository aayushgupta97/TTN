function palindrome() {
var s = prompt("Enter the sting: ")
var rev =  s.split('').reverse().join('')
if(s === rev) {
	alert("is a palindrome")
}
else {
	alert("is not a palindrome")

}
}

palindrome() 