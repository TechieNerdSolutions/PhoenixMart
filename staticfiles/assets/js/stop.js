// function stopLoop(max) 
function stopLoop(max) {
  var count = 0;
  var links = document.querySelectorAll("a[onclick='return stopLoop(max)']");
  for (var i = 0; i < links.length; i++) {
    links[i].onclick = function() {
      if (count >= max) {
        return;
      }
      count++;
      return true;
    };
  }
}



