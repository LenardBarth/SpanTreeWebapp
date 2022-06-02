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
  background-color: whitesmoke;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

/* --- Scrollbar ---
styles imported from:
  https://css-tricks.com/the-current-state-of-styling-scrollbars-in-css/
*/

::-webkit-scrollbar-track
{
  box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  background-color: #F5F5F5;
}

::-webkit-scrollbar
{
  width: 10px;
  background-color: #F5F5F5;
}

::-webkit-scrollbar-thumb
{
  background-color: rgb(18, 18, 18);
  border: 2px solid dimgray;
}
/* --- Scrollbar ---
*/
</style>
