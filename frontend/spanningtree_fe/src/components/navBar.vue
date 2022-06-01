<template>
  <nav>
      <div class="nav-elmts-group" id="left">
        <ul>
          <li><router-link :to="{ name: 'Home' }">Neues Projekt</router-link></li>
          <!-- <li><router-link :to="{ name: '' }"></router-link></li> -->
        </ul>
      </div>
      <div class="nav-elmts-group" id="right">
        <ul>
          <!-- <li><router-link :to="{ name: '' }"></router-link></li> -->
          <!-- <li class="icon" id="account"><router-link :to="{ name: '' }"><img src="@/assets/account.png" alt="Account settings"></router-link></li> -->
          <li class="icon" id="logout"><a v-on:click="logout()"><img src="@/assets/logout_white.png" alt="Log Out"></a></li>
        </ul>
      </div>
  </nav>
</template>

<script>
// import axios from "axios";

export default {
  name: "navBar",
  data() {
      return {}
  },
  methods: {
    async logout() {
    //   const response = await axios.post("auth/api/v1/logout", {}, {
    //     headers: {
    //       "Authorization": "Bearer " + localStorage.token
    //     }
    //   })
    //   if (response.status === 200) {
    //     localStorage.clear()
    //     sessionStorage.clear()
    //     this.$router.push('/login')
    //   } else {
    //     this.$emit('infoPopup', ["err", "Konnte nicht ausgeloggt werden"])
    //     console.log("Logout not completed")
    //   }
    console.log("logout");
    }
  }
}
</script>

<style scoped>
nav {
  position: sticky;
  top: 0;
  width: 100%;
  margin: 0;
  /* padding-top: 25px; */
  display: flex;
  justify-content: space-between;
  background-color: rgba(60, 60, 60);
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

li {
  float: left;
}

li a, li router-link {
  display: block;
  color: white;
  text-align: center;
  padding: 24px 26px;
  text-decoration: none;
  font-weight: bold;
}

.icon img {
  height: 24px;
  width: 24px;
  margin: auto;
}

.icon a {
  padding: 22px 26px;
}

li:hover {
  background-color: rgb(28, 28, 28);
  border-radius: 4px;
}
</style>