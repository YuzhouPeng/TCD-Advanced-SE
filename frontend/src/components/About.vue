<template>
  <div id="about">
    <div id="container">
      <P><span class="title">Team:</span><br>Linghao Ma, Jianan Wei,  Jiongxu Hou, <br>Yuzhou Peng, Yaoling Xie, Yaping Hao</P>
      <p><span class="title">Source Code:</span><br>Open source code locates on <a href="https://github.com/PointerFLY/TCD-Advanced-SE" target="_blank">GitHub</a></p>
      <p><span class="title">Powered By:</span><br>Django Vue.js Docker MySQL Redis</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'about'
}
</script>

<style scoped>
#about {
  overflow-x: hidden;
  overflow-y: scroll;
  width: 100%;
  height: 100%;
}

#container {
  position: relative;
  top: 36%;
  transform: translateY(-50%);
}

p {
  font-size: 1.2em;
  margin: 30px;
}

p .title {
  font-size: 1.3em;
}

</style>
