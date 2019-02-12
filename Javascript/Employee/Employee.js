var listEmp = [ {
	name : "Aayush",
	age : 21 ,
	salary : 9000 , 
	dob : "20/09/97"
},{
	name : "Sarthak",
	age : 19 ,
	salary : 6000 , 
	dob : "31/03/99"
},{
	name : "Kanika",
	age : 21 ,
	salary : 3000 , 
	dob : "24/09/97"
},{
	name : "Hardik",
	age : 19 ,
	salary : 500 , 
	dob : "03/03/99"
},{
	name : "Shivangi",
	age : 30 ,
	salary : 700 , 
	dob : "18/10/88"
}
]

// filtering for salary > 5000
console.log("Filtering for salary > 5000")
for(var i = 0 ; i < listEmp.length ; i++) 
{
  if(listEmp[i].salary > 5000) {
    console.log(listEmp[i]) ; 
  }
} 

console.log("Fetching employees with age more than 30 and salary less than 1000 and incrementing their salary 5 times")
for(var i = 0 ; i < listEmp.length ; i++) 
{
  if(listEmp[i].salary < 1000 && listEmp[i].age > 20) {
    console.log(listEmp[i]) ;
    listEmp[i].salary = listEmp[i].salary * 5 ;  
  }
} 

console.log(listEmp)

console.log("Grouping Employees by Age")
function groupBy(collection, property) {
    var i = 0, val, index,
        values = [], result = [];
    for (; i < collection.length; i++) {
        val = collection[i][property];
        index = values.indexOf(val);
        if (index > -1)
            result[index].push(collection[i]);
        else {
            values.push(val);
            result.push([collection[i]]);
        }
    }
    return result;
}

console.log(groupBy(listEmp, "age"));

