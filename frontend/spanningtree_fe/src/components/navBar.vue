<template>
  <nav>
      <div class="nav-elmts-group" id="left">
        <ul>
          <li><router-link :to="{ name: 'Home' }">New Project</router-link></li>
          <li><router-link :to="{ name: 'Projects' }">My Projects</router-link></li>
        </ul>
      </div>
      <div class="nav-elmts-group" id="right">
        <ul>
          <!-- <li><router-link :to="{ name: '' }"></router-link></li> -->
          <!-- <li class="icon" id="account"><router-link :to="{ name: '' }"><img src="@/assets/account.png" alt="Account settings"></router-link></li> -->
          <li class="icon" id="logout" v-if="logged_in==='True'"><a v-on:click="logout()"><img src="@/assets/logout_white.png" alt="Log Out"></a></li>
          <li class="icon" v-if="logged_in==='False'"><router-link :to="{ name: 'Login' }">Login</router-link></li>
          <li class="icon" v-if="logged_in==='False'"><router-link :to="{ name: 'Register' }">Sign Up</router-link></li>
        </ul>
      </div>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "navBar",
  data() {
      return {
        logged_in: localStorage.getItem('logged_in') ? localStorage.getItem('logged_in') : "False"
      }
  },
  methods: {
    async logout() {
      const response = await axios.post("auth/logout", {'user_id': parseInt(localStorage.getItem('userid'))}).catch(err => {
        console.log("error: ", err);
      })
      if (response && response.status === 200) {
        localStorage.clear()
        this.$router.push({ name: 'Login'})
        this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
      } else {
        this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
      }
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