<template>
  <div id="station">
    <div id="map" ref="map"></div>
  </div>
</template>

<script>
export default {
  name: 'station',
  map: null,
  created () {
    let GoogleMap = require('google-maps')
    GoogleMap.KEY = 'AIzaSyAN-k2Z0JpTVPPzGkt61YImxgxTf4PUzk0'
    GoogleMap.LANGUAGE = 'en'

    GoogleMap.load(google => {
      let canvas = this.$refs.map
      let options = {
        center: new google.maps.LatLng(53.343507, -6.253920),
        zoom: 16
      }
      this.map = new google.maps.Map(canvas, options)
    })
  }
}
</script>

<style scoped>
#station {
  color: #fff;
  background-color: #fff;
  width: 100%;
  height: 100%;
}

#map {
  width: 100%;
  height: 100%;
}
</style>
