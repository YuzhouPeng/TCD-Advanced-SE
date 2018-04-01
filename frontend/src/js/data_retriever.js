'use strict'

const URL = 'http://localhost/'

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
    setTimeout(this._fetch(), 1000)
  }

  _fetch () {
    let urls = {
      busRealtime: URL + 'bus_realtime',
      busStations: URL + 'bus_stations',
      bikeRealtime: URL + 'bike_realtime'
    }
    let e = new Event(DataRetriever.DATA_UPDATED_EVENT)
    let count = 0
    for (let key in urls) {
      let xmlHttp = new XMLHttpRequest()
      xmlHttp.open('GET', urls[key], true)
      xmlHttp.onload = () => {
        count++
        e[key] = xmlHttp.responseText
        if (count === Object.keys(urls).length) {
          dispatchEvent(e)
        }
      }
      xmlHttp.send()
    }
  }
}
