<template>
  <div id="app">
    <header id="header">
      <div id="header-brand"><span class="highlight">Dublin City</span> Management</div>
      <div id="header-title">{{views[currentIndex].title}}</div>
      <div id="header-logout" @click="logout">Log out</div>
    </header>

    <section id="sidebar">
      <ul>
        <li v-for="(view, index) in views" :key="index" :index="index" :class="['bar-item', {'active' : index === currentIndex}]" @click="changeView">{{view.title}}</li>
      </ul>
    </section>

    <section id="view">
      <router-view></router-view>
    </section>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      currentIndex: 0,
      views: [
        {
          title: 'Station',
          route: '/'
        },
        {
          title: 'Emission',
          route: '/emission'
        },
        {
          title: 'Monitor',
          route: '/monitor'
        },
        {
          title: 'About',
          route: '/about'
        }
      ]
    }
  },
  methods: {
    logout () {
      // TODO: Logout
    },
    changeView (e) {
      let index = parseInt(e.target.getAttribute('index'))
      if (this.currentIndex !== index) {
        this.$router.push(this.views[index].route)
        this.currentIndex = index
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Arial, Helvetica, sans-serif;
  text-align: center;
}

html, body {
  padding: 0;
  margin: 0;
  border: 0;
  width: 100%;
  height: 100%;
}

/* header */

#header {
  width: 100%;
  height: 50px;
  background: #272b30;
  position: fixed;
  text-align: center;
}

#header div {
  color: #fff;
  display: inline-block;
  line-height: 50px;
  padding: 0 12px;
}

#header-brand {
  float: left;
  font-size: 1.3em;
}

#header .highlight {
  color: #e8491d;
  font-weight: bold;
}

#header-title {
  font-size: 1.7em;
}

#header-logout {
  font-size: 1.0em;
  opacity: 0.7;
  float: right;
}

#header-logout:hover {
  opacity: 1.0;
  color:#ffffff;
  text-decoration:none;
  cursor: pointer;
}

/* sidebar */

#sidebar {
  position: fixed;
  top: 50px;
  width: 240px;
  height: calc(100vh - 50px);
  border-right: 1px solid #ddd;
  flex-grow: 100;
  overflow: visible;
  background-color: #f2f4f6;
}

#sidebar ul {
  padding: 0;
  margin: 0;
  list-style: none;
}

.bar-item {
  width: 240px;
  height: 80px;
  line-height: 80px;
  text-align: center;
  font-size: 1.2em;
  cursor: pointer;
}

.bar-item:hover {
  color: #e8491d;
}

.bar-item.active {
  color: #e8491d;
  background-color: #fff;
}

#view {
  position: fixed;
  top: 50px;
  left: 241px;
  width: calc(100vw - 241px);
  height: calc(100vh - 50px);
  background-color: #fff;
}
</style>
