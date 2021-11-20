let headphonesImg = document.getElementById('imgHeadphonesForSounds');
headphonesImg.setAttribute('src', 'img/no-headphones.png');

function ChangeimgHeadphonesForSounds(){
    let isItOn = headphonesImg.getAttribute('src');
    if(isItOn === 'img/no-headphones.png'){
        headphonesImg.setAttribute('src', 'img/headphones.png')
    } else if(isItOn === 'img/headphones.png'){
        headphonesImg.setAttribute('src', 'img/no-headphones.png')
}};