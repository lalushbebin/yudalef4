var elements = document.getElementById('CodeArea').children
Array.from(elements).forEach(function(elt){
  elt.addEventListener("keyup", function(event) {
  console.log(event)
    if (elt.value.length == 1) {
      // Focus on the next sibling
      console.log(elt.value)
      elt.nextElementSibling.focus()
    }
  });
})