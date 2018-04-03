import DataRetriever from "./data-retriever";

export function initMap() {
  this.map = new google.maps.Map(document.getElementById('map-emission'), {
    zoom: 11,
    center: {lat: 53.343507, lng: -6.253920},
    mapTypeId: 'satellite'
  });

  pointLisener()
}

function pointLisener() {
  addEventListener(DataRetriever.DATA_UPDATED_EVENT, function (e) {
    let points = []
    for (let i = 0; i < e.busStations.length; i++) {
      if (e.busRealtime[e.busStations[i].ID]) {
        points.push({
          location: new google.maps.LatLng(e.busStations[i].latitude, e.busStations[i].longitude),
          weight: (e.busRealtime[e.busStations[i].ID].emmision_level * 10)
        })
      }
    }

    let heatmap = new google.maps.visualization.HeatmapLayer({
      data: points,
      map: map
    });
  })
}

export function loadGoogleMap() {
  let script = document.createElement("script");
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyAN-k2Z0JpTVPPzGkt61YImxgxTf4PUzk0&libraries=visualization&callback=initMap";
  script.type = "text/javascript";
  document.getElementsByTagName("head")[0].appendChild(script);
}
