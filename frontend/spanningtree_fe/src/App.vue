<template>

  <navBarVue />
  <router-view @infoPopup="handleInfo($event)" />
  <userInfoPopupVue v-if="this.infoMsg.msg !== ''" v-show="showInfo" :info="this.infoMsg" />

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
      infoMsg: {status: "", msg: ""},
      showInfo: false
    }
  },
  methods: {
    handleInfo(_info) {
      console.log(_info)
      this.infoMsg = _info
      this.showInfo = true
      setTimeout(() => {
        this.showInfo = false
        this.infoMsg.msg = ''
      }, 2500)
    }
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
  margin: 0;
  padding: 0;
}
</style>
