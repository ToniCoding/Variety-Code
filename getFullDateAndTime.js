// Get the current UTC date and time with 2 digits format.

const dateObject = new Date();
var currentTime = String(dateObject.getUTCHours()).padStart(2, '0') + ':' + String(dateObject.getUTCMinutes()).padStart(2, '0') + ':' + String(dateObject.getUTCSeconds()).padStart(2, '0');
var currentDate = String(dateObject.getUTCMonth() + 1).padStart(2, '0') + '-' + String(dateObject.getUTCDate()).padStart(2, '0') + '-' + String(dateObject.getUTCFullYear()).padStart(2, '0');
var dateTime = `${currentDate}, ${currentTime}`; 

console.log(dateTime);