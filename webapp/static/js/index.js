var input = document.getElementById("req");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById("launchbtn").click();
  }
});

function launch() {
        req = document.getElementById("req").value
        var xhr = new XMLHttpRequest();
        console.log("working fine")
        xhr.open("GET", "http://127.0.0.1:5000/launch?req=" + req, true);
        xhr.send();
        xhr.onload = function () {
                var output = xhr.responseText;
                document.getElementById("output").innerHTML = output;
        }
}

function voice() {
        wake = document.getElementById("wake").value
        var xhr = new XMLHttpRequest();
        console.log("working fine")
        xhr.open("GET", "http://127.0.0.1:5000/voice?wake=" + wake, true);
        xhr.send();
        xhr.onload = function () {
                var output = xhr.responseText;
                document.getElementById("output").innerHTML = output;
        }
}