'use strict';

import DataRetriever from "./data_retriever.js";

export default class MapController {

    constructor() {
        let canvas = document.getElementById('map');
        let options = {
            center: new google.maps.LatLng(53.343507, -6.253920),
            zoom: 16
        };
        this.map = new google.maps.Map(canvas, options);

        this.addListeners();
    }

    addListeners() {
        addEventListener(DataRetriever.DATA_UPDATED_EVENT, function (e) {
            alert(e.bikeRealtime);
            alert(e.busRealtime);
            alert(e.busStations);
            // update map markers
        });
    }

    _updateMarkers() {
    }
}