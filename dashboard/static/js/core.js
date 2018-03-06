let selectedIndex = 0;
let views = null;
let barItems = null;
let headerTitle = null;
let titles = ['Station', 'Emission', 'Monitor', 'About'];

document.write('<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAN-k2Z0JpTVPPzGkt61YImxgxTf4PUzk0&language=en"></script>')

window.onload = function() {
    init();
    addEvents();
    loadMap();
};

function init() {
    views = document.getElementsByClassName('view');
    barItems = document.getElementsByClassName('sidebar-item');
    headerTitle = document.getElementById('header-title');

    barItems[selectedIndex].style.backgroundColor = '#fff';
    barItems[selectedIndex].style.color = '#e8491d';
    for (let view of views) {
        view.style.visibility = 'hidden';
    }
    views[selectedIndex].style.visibility = 'visible';
}

function loadMap() {
    let canvas = document.getElementById('map');
    let options = {
        center: new google.maps.LatLng(53.343507, -6.253920),
        zoom: 16
    };
    new google.maps.Map(canvas, options);
}

function addEvents() {
    for (let item of barItems) {
        item.addEventListener('mouseup', function(event) {
            let target = event.target
            if (target === barItems[selectedIndex]){ return; }
            let idx = [].indexOf.call(barItems, target);

            target.style.backgroundColor = '#fff';
            target.style.color = '#e8491d';
            barItems[selectedIndex].style.backgroundColor = '#f2f4f6';
            barItems[selectedIndex].style.color = '#000';
            views[selectedIndex].style.visibility = 'hidden';
            views[idx].style.visibility = 'visible';
            headerTitle.innerHTML = titles[idx];

            selectedIndex = [].indexOf.call(barItems, target);
        });
        item.addEventListener('mouseenter', function(event) {
            if (event.target === barItems[selectedIndex]){ return; }
            event.target.style.color = '#e8491d';
        });
        item.addEventListener('mouseout', function(event) {
            if (event.target === barItems[selectedIndex]){ return; }
            event.target.style.color = '#000';
        })
    }
}
