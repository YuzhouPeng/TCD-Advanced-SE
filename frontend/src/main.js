// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import * as VueResource from 'vue-resource'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import DataRetriever from './js/data-retriever'
import MapController from './js/map-controller'

Vue.config.productionTip = false
Vue.use(VueResource)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

let dataRetriever = new DataRetriever()
dataRetriever.start()

/* eslint-disable no-new */
new MapController()
