<template>
  <div class="LoginMaskWrapper">
    <h1>Login</h1>
    <form @submit.prevent="handleSubmit">
        <input type="text" id="email" name="email" autocomplete="email" v-model="email" required placeholder="Email" />
        <input type="password" id="password" name="password" autocomplete="current-password" v-model="password" required placeholder="Password" />
        <br><br>
        <button type="submit" class="btn btn-primary btn-lg">Login</button>
    </form>
    <button @click="this.$router.push({ name: 'Register'})" class="btn btn-outline-secondary btn-lg">New Account</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginMask',
  emits: ['infoPopup'],
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async handleSubmit() {
      const response = await axios.post('auth/login', {
        "email": this.email,
        "password": this.password
      }).catch(err => {
        console.log(err)
        this.$emit('infoPopup', {status: "danger", msg: "Login error"})
      })
      if (response && response.status === 200) {
        console.log("response:", response);
        if (response.data.status === 'success') {
          localStorage.setItem('user_id', toString(response.data.user_id))
          localStorage.setItem('logged_in', "True")
          this.$router.push({ name: 'Home'})
        }
        this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
      } else {
          this.$emit('infoPopup', {status: "danger", msg: "Could not reach Server"})
      }
    }
  }
}
</script>

<style scoped>
  .LoginMaskWrapper {
    background: rgba(60, 60, 60);
    margin: 15vh auto;
    padding: 25px;
    top: 10vh;
    width: 50vw;
    max-width: 750px;
    min-width: 300px;
    min-height: 400px;
    border: 2px solid gray;
    border-radius: 15px;
    box-shadow: inset 0 0 1em black;
    color: white;
    letter-spacing: 2px;
  }

  input {
    width: 66%;
    height: 30px;
    margin: 2.5% 10%;
    padding: 20px;
    font-size: medium;
    border-radius: 30px;
  }

  button {
      margin: 5px
  }
</style>