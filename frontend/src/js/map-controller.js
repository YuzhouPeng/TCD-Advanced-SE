'use strict'

import DataRetriever from './data-retriever'
import GoogleMap from 'google-maps'

export default class MapController {
  constructor () {
    GoogleMap.KEY = 'AIzaSyAN-k2Z0JpTVPPzGkt61YImxgxTf4PUzk0'
    GoogleMap.LANGUAGE = 'en'

    GoogleMap.load(google => {
      let canvas = document.getElementById('map-station')
      let options = {
        center: new google.maps.LatLng(53.343507, -6.253920),
        zoom: 16
      }
      this.map = new google.maps.Map(canvas, options)
    })

    this.addListeners()
  }

  addListeners() {
    let that = this
    addEventListener(DataRetriever.DATA_UPDATED_EVENT, function (e) {
      parseToJson(e)
      let bikeIcon = "http://127.0.0.1:8887/bike_icon.png"
      let busIcon = "http://127.0.0.1:8887/bus_icon.png"
      for (let i = 0; i < e.bikeRealtime.length; i++) {
        let contentString = '<div id="content">' +
          '<div id="siteNotice">' + '</div>' +
          '<h3 id="firstHeading" style="color: black" class="firstHeading">' +
          e.bikeRealtime[i].name + '<br>' +
          'Available bikes: ' + e.bikeRealtime[i].bike_available + '<br>' +
          'Free stands: ' + (e.bikeRealtime[i].bike_stands - e.bikeRealtime[i].bike_available) +
          '</h3>'

        createMarker(e.bikeRealtime[i], contentString, bikeIcon)
      }

      let busRoutesString
      for (let i = 0; i < e.busStations.length; i++) {
        if (e.busRealtime[e.busStations[i].ID]) {
          let commingRoutes = e.busRealtime[e.busStations[i].ID].comming_routes
          busRoutesString = "<table style=\"width:100%; color: black\"><tr>" +
            "    <th>Route</th>" +
            "    <th>Direction</th>" +
            "    <th>Source Time</th>" +
            "    <th>Arriveal Time</th>" +
            "    <th>Scheduled Time</th>" +
            "  </tr>"
          for (let j = 0; j < commingRoutes.length; j++) {
            busRoutesString = busRoutesString +
              "<tr>" +
              "    <td align=\"center\">" + commingRoutes[j].route + "</td>" +
              "    <td align=\"center\">" + commingRoutes[j].direction + "</td>" +
              "    <td align=\"center\">" + commingRoutes[j].source_time.slice(-8) + "</td>" +
              "    <td align=\"center\">" + commingRoutes[j].arriveal_time.slice(-8) + "</td>" +
              "    <td align=\"center\">" + commingRoutes[j].scheduled_time.slice(-8) + "</td>" +
              "</tr>"
          }
        } else {
          busRoutesString = "No comming bus."
        }

        let contentString = '<div id="content">' +
          '<div id="siteNotice">' + '</div>' +
          '<h3 id="firstHeading" style="color: black" class="firstHeading">' +
          'No.' + e.busStations[i].ID + ': ' + e.busStations[i].name + '<br>' +
          'Routes: ' + e.busStations[i].routes + '<br>' +
          '</h3>' + busRoutesString

        createMarker(e.busStations[i], contentString, busIcon)
      }


      let infoWindow = new google.maps.InfoWindow({})

      function parseToJson(e) {
        for (let i = 1; i < Object.keys(e).length; i++) {
          e[Object.keys(e)[i]] = JSON.parse(e[Object.keys(e)[i]])
        }
      }

      function createMarker(mark, contentString, icon) {
        let marker = new google.maps.Marker({
          position: new google.maps.LatLng(mark.latitude, mark.longitude),
          map: that.map,
          title: mark.name,
          contentString: contentString,
          icon: icon
        })
        google.maps.event.addListener(marker, 'click', function () {
          infoWindow.setContent(marker.contentString)
          infoWindow.open(this.map, marker)
          that.map.panTo(marker.getPosition())
        })
      }
    })
  }
}
