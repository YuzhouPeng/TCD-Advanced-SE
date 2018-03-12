'use strict';

export function loadMap() {
    let canvas = document.getElementById('map');
    let options = {
        center: new google.maps.LatLng(53.343507, -6.253920),
        zoom: 16
    };
    new google.maps.Map(canvas, options);
}

function startFetchLoop() {
    function fetch() {
        let request = new XMLHttpRequest();
        request.open('get', '/bus_stations', true);
        request.send();
        request.onReadyStateChange = function() {
            updateBusStations();
            updateBikeStations();
        }
    }
    setTimeout(fetch, 6000);
}

function updateBikeStations() {

}

function updateBusStations() {

}

function showMap() {
     let marker = new google.maps.Marker({
        position: new google.maps.LatLng(stationsLocations[i][2], stationsLocations[i][3]),
        map: map,
        title: stationsLocations[i][1],
        contentString: contentString
    });

    marker.addEventListener('click', function () {
        infoWindow.setContent(this.contentString);
        infoWindow.open(map, this);
        map.panTo(this.getPosition())
    })
}
