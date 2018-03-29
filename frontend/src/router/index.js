import Vue from 'vue'
import Router from 'vue-router'
import About from '@/components/About'
import Emission from '@/components/Emission'
import Monitor from '@/components/Monitor'
import Station from '@/components/Station'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', component: Station },
    { path: '/emission', component: Emission },
    { path: '/monitor', component: Monitor },
    { path: '/about', component: About }
  ]
})
