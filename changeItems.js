let theHTMLItem = document.getElementById('itemToSwitch');
theHTMLItem.setAttribute('attributeToChange', 'valueOfAttribute');

function itemSwitcher(){
    let itemActualStatus = theHTMLItem.getAttribute('attributeToChange');
    if(itemActualStatus === 'newValue'){
        theHTMLItem.setAttribute('attributeToChange', 'valueOfAttribute')
    } else if(itemActualStatus === 'newValue'){
        theHTMLItem.setAttribute('attributeToChange', 'valueOfAttribute')
}};
