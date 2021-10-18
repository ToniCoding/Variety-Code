// Script that changes the class of the body to alter the background in the index page depending on the local UTC.

isDate = new Date();
var isHours = isDate.getHours();

if(isHours >= 8 && isHours <= 11){
    document.getElementById('indexBG').classList.remove('indexBGNone');
    document.getElementById('indexBG').classList.add("indexBGMorning");
}

if (isHours >=15 && isHours <= 18) {
    document.getElementById('indexBG').classList.remove('indexBGNone');
    document.getElementById('indexBG').classList.add("indexBGAfternoon");
}

if (isHours >= 19 && isHours <= 20) {
    document.getElementById('indexBG').classList.remove('indexBGNone');
    document.getElementById('indexBG').classList.add("indexBGAfternoon2");
}

if (isHours >= 21 && isHours <= 23) {
    document.getElementById('indexBG').classList.remove('indexBGNone');
    document.getElementById('indexBG').classList.add("indexBGNight");
}

if (isHours >= 0 && isHours <= 7) {
    document.getElementById('indexBG').classList.remove('indexBGNone');
    document.getElementById('indexBG').classList.add("indexBGMidnight");
}