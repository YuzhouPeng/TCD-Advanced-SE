<template>
  <div id="monitor">
    <div class="container">
      <div class="col-md-5 mb-3 select-div">
        <label class="select-label">Bus station emission alert threshold</label>
        <select v-model="selected" class="custom-select d-block w-100" required>
          <option disabled :value="busThreshold">Please select one</option>
          <option v-for="option in busThresholdOptions" :key="option.id" :value="option">{{option}}</option>
        </select>
      </div>

      <div class="col-md-5 mb-3 select-div">
        <label class="select-label">Bike station available bike alert threshold</label>
        <select class="custom-select d-block w-100" required>
          <option disabled :value="bikeThrehold">Please select one</option>
          <option v-for="option in bikeThresholdOptions" :key="option.id" :value="option">{{option}}</option>
        </select>
      </div>

      <div class="col-md-5 mb-3 select-div">
        <label class="select-label">Type: Bike or Bus</label>
        <select class="custom-select d-block w-100" required>
          <option v-for="option in types" :key="option.id" :value="option">{{option}}</option>
        </select>
      </div>

      <div class="col-md-5 mb-3 select-div">
        <label class="select-label">Choose from available times</label>
        <select class="custom-select d-block w-100" required>
          <option v-for="option in times" :key="option.id" :value="option">{{option}}</option>
        </select>
      </div>

      <table class="table table-bordered">
        <thead class="thead-light">
        <tr><th v-for="head in headTitles" :key="head.id">{{head}}</th></tr>
        </thead>
        <tbody>
        <tr v-for="stop in filteredStops" :key="stop.id">
          <th>{{stop.time}}</th>
          <th>{{stop.type}}</th>
          <td>{{stop.id}}</td>
          <td>{{stop.name}}</td>
          <td>{{stop.emissionLevel}}</td>
          <td>{{stop.availableBike}}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import DataRetriever from "../js/data-retriever";

export default {
  name: 'monitor',
  data () {
    return {
      headTitles: ['Time', 'Type', 'Stop ID', 'Stop Name', 'Emission Level', 'Available Bike'],
      busThresholdOptions: [1, 2, 3, 4, 6, 7, 8],
      bikeThresholdOptions: [1, 2, 3, 4, 5, 6, 7, 8],
      types: ['Bus', 'Bike', 'Both'],
      times: ['18:00', '19:00', '21:00'],
      bikeThreshold: 5,
      busThreshold: 1,

      alertStops: []
    }
  },
  computed: {
    filteredStops () {
      console.log(this.bikeThreshold)
      return this.alertStops.filter( stop =>
        stop.availableBike < this.bikeThreshold ||
        stop.emissionLevel > this.busThreshold
      )
    }
  },
  created () {
    let that = this
    addEventListener(DataRetriever.DATA_UPDATED_EVENT, (e) => {
      let keys = Object.keys(e)
      for (let i = 1; i < keys.length; i++) {
        e[keys[i]] = JSON.parse(e[keys[i]])
      }
      // console.log(that.alertStops[0].availableBike)
      for (let i = 0; i < e.bikeRealtime.length; i++) {
        that.alertStops.push({
          time: null,
          type: 'bike',
          id: null,
          name: e.bikeRealtime[i].name,
          availableBike: e.bikeRealtime[i].bike_available,
          emissionLevel: null
        })
      }
    })
  }
}
</script>

<style scoped>
.select-div {
  display: inline-block;
}

#monitor {
  overflow-y: scroll;
  width: 100%;
  height: 100%;
}

.container {
  padding-top: 16px;
}

.select-label {
  font-size: 1.05em;
}
</style>
