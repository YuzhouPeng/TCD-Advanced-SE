'use strict';

import DataRetriever from "./data_retriever.js";

export default class MapController {

    constructor() {
        this.canvas = document.getElementById('map');
        this.options = {
            center: new google.maps.LatLng(53.343507, -6.253920),
            zoom: 16
        };
        this.map = new google.maps.Map(this.canvas, this.options);

        this.addListeners();
    }

    addListeners() {
        let that = this;
        addEventListener(DataRetriever.DATA_UPDATED_EVENT, function (e) {
            parseToJson(e);
            let bikeIcon = "dashboard/static/img/bike_ico.png";
            let busIcon = "dashboard/static/img/bus_ico.png";
            for (let i = 0; i < e.bikeRealtime.length; i++) {
                let contentString = '<div id="content">' +
                    '<div id="siteNotice">' + '</div>' +
                    '<h1 id="firstHeading" class="firstHeading">' +
                    e.bikeRealtime[i].name + '<br>' +
                    'Available bikes: ' + e.bikeRealtime[i].bike_available + '<br>' +
                    'Free stands: ' + (e.bikeRealtime[i].bike_stands - e.bikeRealtime[i].bike_available) +
                    '</h1>';

                createMarker(e.bikeRealtime[i], contentString, bikeIcon)
            }

            for (let i = 0; i < e.busStations.length; i++) {
                let contentString = '<div id="content">' +
                    '<div id="siteNotice">' + '</div>' +
                    '<h1 id="firstHeading" class="firstHeading">' +
                    'No.' + e.busStations[i].ID + ': ' + e.busStations[i].name + '<br>' +
                    'Routes: ' + e.busStations[i].routes + '<br>' +
                    '</h1>';

                createMarker(e.busStations[i], contentString, busIcon)
            }


            let infoWindow = new google.maps.InfoWindow({});

            function parseToJson(e) {
                for (let i = 1; i < Object.keys(e).length; i++) {
                    e[Object.keys(e)[i]] = JSON.parse(e[Object.keys(e)[i]]);
                }
            }

            function createMarker(mark, contentString, icon) {
                let marker = new google.maps.Marker({
                    position: new google.maps.LatLng(mark.latitude, mark.longitude),
                    map: that.map,
                    title: mark.name,
                    contentString: contentString,
                    icon: icon
                });
                google.maps.event.addListener(marker, 'click', function () {
                    infoWindow.setContent(marker.contentString);
                    infoWindow.open(map, marker);
                    that.map.panTo(marker.getPosition())
                });
            }

        });
    }

    _updateMarkers() {
    }
}