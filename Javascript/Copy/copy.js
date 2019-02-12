A = {name : "Aayush",
	 age : 21,
	 isIntern : true }

console.log("object A is " , A)

var B = JSON.parse(JSON.stringify(A));
console.log("object B is " , B)
console.log("object A is " , A)

