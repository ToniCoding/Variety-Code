// Script that greet the user depending on the time of the day.


var isDay = new Date();
var isTime = isDay.getHours();

if(isTime >= 6 && isTime <= 12){
document.getElementById("greet").innerHTML = "Good morning! ";
}

if (isTime >= 13 && isTime <= 20){
document.getElementById("greet").innerHTML = "Good afternoon! ";
}

if (isTime >= 21){
    document.getElementById("greet").innerHTML = "Good night! ";
}

if (isTime >=0 && isTime < 6){
    document.getElementById("greet").innerHTML = "Good night! ";
}