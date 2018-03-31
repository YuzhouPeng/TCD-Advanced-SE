<template>
  <div id="monitor" class="container">
    <div class="col-md-5 mb-3">
      <label class="select-label">Bus station emission alert threshold</label>
      <select class="custom-select d-block w-100" required>
        <option v-for="option in busOptions" :key="option.id" :value="option">{{option}}</option>
      </select>
    </div>

    <table class="table table-bordered">
      <thead class="thead-light">
      <tr><th v-for="head in busHeads" :key="head.id">{{head}}</th></tr>
      </thead>
      <tbody>
      <tr v-for="stop in alertedBusStops" :key="stop.id">
        <th scope="row">{{stop.date}}</th>
        <td>{{stop.id}}</td>
        <td>{{stop.name}}</td>
        <td>{{stop.emissionLevel}}</td>
      </tr>
      </tbody>
    </table>

    <div id="mid-divider"></div>

    <div class="col-md-5 mb-3">
      <label class="select-label">Bike station available bike alert threshold</label>
      <select class="custom-select d-block w-100" required>
        <option v-for="option in bikeOptions" :key="option.id" :value="option">{{option}}</option>
      </select>
    </div>

    <table class="table table-bordered">
      <thead class="thead-light">
      <tr><th v-for="head in bikeHeads" :key="head.id">{{head}}</th></tr>
      </thead>
      <tbody>
      <tr v-for="stop in alertedBikeStops" :key="stop.id">
        <th scope="row">{{stop.date}}</th>
        <td>{{stop.id}}</td>
        <td>{{stop.name}}</td>
        <td>{{stop.availableCount}}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'monitor',
  data () {
    return {
      busHeads: ['Date', 'Stop ID', 'Stop Name', 'Emission Level'],
      bikeHeads: ['Date', 'Stop ID', 'Stop Name', 'Bike Available'],
      busOptions: [1, 2, 3, 4, 6, 7, 8],
      bikeOptions: [1, 2, 3, 4, 5, 6, 7, 8],

      alertedBusStops: [
        {
          date: '18:00',
          id: '123',
          name: '1213',
          emissionLevel: 200
        },
        {
          date: '18:00',
          id: '123',
          name: '1213',
          emissionLevel: 100
        }
      ],
      alertedBikeStops: [
        {
          date: '18:00',
          id: '123',
          name: '1213',
          availableCount: 10
        },
        {
          date: '18:00',
          id: '123',
          name: '1213',
          availableCount: 12
        }
      ],
    }
  }
}
</script>

<style scoped>
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

#mid-divider {
  height: 12px;
}
</style>
