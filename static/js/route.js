var nav_ = document.getElementsByTagName('nav')[0];
var main_ = document.getElementsByTagName('main')[0];
var title_ = document.getElementsByClassName('mdl-layout-title')[0];

function addEventListener(item, index){
    if (typeof item.id !== 'undefined') {
        document.getElementById(item.id).addEventListener('click', function(event) {
            var xhttp = new XMLHttpRequest();
            xhttp.addEventListener('load', function(response){
                // this isn't fast, but it works
                title_.innerHTML = (item.id.charAt(0).toUpperCase() + item.id.slice(1)).replace(/_/, ' ');
                main_.innerHTML = response.target.responseText;
            });
            xhttp.open('GET', event.target.href);
            xhttp.send();
            event.preventDefault();
        });
    }
}

nav_.childNodes.forEach(addEventListener);
