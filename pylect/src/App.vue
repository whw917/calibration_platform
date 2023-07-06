<template>
  <div id="app">
    <NavigationMenu />
    <span style="font-size:32px;color:blue;margin-bottom:20px">角度标定系统</span>
    <router-view/>
  </div>
</template>

<script>
import NavigationMenu from '@/views/NavigationMenu.vue'

export default {
  name: 'App',
  components: {
    NavigationMenu
  }
}
</script>

<style>
html{
  height: 95%;
}

body{
  height: 95%;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
  height: 100%;
}
</style>
