let percentage = document.getElementById('percentageLoader');
let progress = 0;
let refresh = setInterval(progressNumb, 30);

function progressNumb(){
    progress += 1;
    percentage.innerHTML = progress;
    if(progress >= 100){
        clearInterval(refresh);
    };
};