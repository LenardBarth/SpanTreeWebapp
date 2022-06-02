<template>

  <navBarVue />
  <router-view @infoPopup="handleInfo($event)" />
  <div class="infostack" v-if="this.infoStack !== []">
    <userInfoPopupVue v-for="infoMsg in infoStack" :key="infoMsg.status + infoMsg.msg" :info="infoMsg" />
  </div>

</template>

<script>
import navBarVue from "./components/navBar.vue";
import userInfoPopupVue from "./components/userInfoPopup.vue";

export default {
  components: {
    navBarVue,
    userInfoPopupVue,
  },
  data() {
    return {
      infoStack: [],
    }
  },
  methods: {
    handleInfo(_info) {
      this.infoStack.push(_info)
    }
  }
}
</script>

<style>
#app {
  height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}
</style>
