<template>
  <div id="monitor">
    <div class="container">
      <div class="col-md-5 mb-3 select-div">
        <label class="select-label">Bus station emission alert threshold</label>
        <select class="custom-select d-block w-100" required>
          <option v-for="option in busThresholdOptions" :key="option.id" :value="option">{{option}}</option>
        </select>
      </div>

      <div class="col-md-5 mb-3 select-div">
        <label class="select-label">Bike station available bike alert threshold</label>
        <select class="custom-select d-block w-100" required>
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
        <tr v-for="stop in alertStops" :key="stop.id">
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
export default {
  name: 'monitor',
  data () {
    return {
      headTitles: ['Time', 'Type', 'Stop ID', 'Stop Name', 'Emission Level', 'Available Bike'],
      busThresholdOptions: [1, 2, 3, 4, 6, 7, 8],
      bikeThresholdOptions: [1, 2, 3, 4, 5, 6, 7, 8],
      types: ['Bus', 'Bike', 'Both'],
      times: ['18:00', '19:00', '21:00'],

      alertStops: [
        {
          time: '18:00',
          type: 'bus',
          id: '123',
          name: '1213',
          availableBike: 12,
          emissionLevel: null
        },
        {
          time: '18:00',
          type: 'bike',
          id: '123',
          name: '1213',
          availableBike: null,
          emissionLevel: 100
        },
        {
          time: '18:00',
          type: 'bike',
          id: '123',
          name: '1213',
          availableBike: null,
          emissionLevel: 100
        },
      ]
    }
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
