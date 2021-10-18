function filterResources() {

    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('userInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("theResourcesList");
    li = ul.getElementsByTagName('li');
  

    for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {  // In case of doing the filter case sensitive, remove the method .toUpperCase.
        li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
  }