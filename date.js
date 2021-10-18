// Tells the user the complete date DD/MM/YYYY.
var isDate = new Date();

document.getElementById("date").innerHTML = "Today is: " + isDate.getDate() + "/" + (isDate.getMonth()+1) + "/" + isDate.getFullYear();