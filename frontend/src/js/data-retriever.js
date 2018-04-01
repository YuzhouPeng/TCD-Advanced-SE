'use strict'

const URL = 'http://localhost:8000/'
const FETCH_INTERVAL = 1000 * 180

export default class DataRetriever {
  constructor () {
    this.jsonBusRealtime = null
    this.jsonBusStations = null
    this.jsonBikeRealtime = null
  }

  static get DATA_UPDATED_EVENT () {
    return 'DATA_UPDATED_EVENT'
  }

  start () {
    setTimeout(this._fetch(), FETCH_INTERVAL)
  }

  _fetch () {
    let urls = {
      busRealtime: URL + 'bus_realtime',
      busStations: URL + 'bus_stations',
      bikeRealtime: URL + 'bike_realtime'
    }

    let event = new Event(DataRetriever.DATA_UPDATED_EVENT)
    let requestedCount = 0

    for (let url in urls) {
      let request = new XMLHttpRequest()
      request.open('GET', urls[url], true)
      request.onload = () => {
        event[url] = request.responseText

        requestedCount++
        if (requestedCount === Object.keys(urls).length) {
          dispatchEvent(event)
        }
      }
      request.send()
    }
  }
}
