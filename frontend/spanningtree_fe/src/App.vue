<template>
  <navBarVue />
  <router-view />
</template>

<script>
import navBarVue from "./components/navBar.vue";

export default {
  components: {
    navBarVue,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
