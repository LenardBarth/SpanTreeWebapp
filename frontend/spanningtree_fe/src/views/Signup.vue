<template>
  <div class="jumbotron">
      <h1>Create Account</h1>
      <h4>Personal data will only be used to associate projects to you as a User</h4>
      <div class="form-wrapper">
        <form @submit.prevent="handleSubmit">
          <input type="text" id="email" name="email" autocomplete="email" minlength="4" v-model="email" required placeholder="Email" />
          <div class="input-grouped-2">
              <input type="text" id="first_name" name="first_name" v-model="first_name" required placeholder="First Name" />
              <input type="text" id="last_name" name="last_name" v-model="last_name" required placeholder="Last Name" />
          </div>
          <input type="password" id="password" name="password" minlength="4" v-model="password" required placeholder="Password" />
          <input type="password" id="password_repeat" name="password_repeat" v-model="password_repeat" required placeholder="Repeat password" />
          <br><br>
          <button type="submit" class="btn btn-primary btn-lg">Submit</button>
        </form>
        <button @click="this.$router.push({ name: 'Login'})" class="btn btn-outline-secondary btn-lg">Login with existing account</button>
      </div>
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
      first_name: '',
      last_name: '',
      password: '',
      password_repeat: ''
    }
  },
  methods: {
    // checks if entered data is passable
    handleSubmit() {
      // only continue if passwords match
      if (this.password===this.password_repeat) {
          this.sendSignUp()
      } else {
          this.$emit('infoPopup', {status: "warning", msg: "Passwords did not match. Please try again!"})
          this.password = ''
          this.password_repeat = ''
      }
    },
    // sneds signup request to backend to create new user with given data
    async sendSignUp() {
      const response = await axios.post('auth/createUser', {
          "email": this.email,
          "first_name": this.first_name,
          "last_name": this.last_name,
          "password": this.password,
          "password_repeat": this.password_repeat
      }).catch(err => {
          console.log(err)
          this.$emit('infoPopup', {status: "danger", msg: "Signup error"})
      })
      // if request wass successful
      if (response && response.status === 200) {
        // if backend did not throw any errors
        if (response.data.status === 'success') {
          this.$router.push({ name: 'Home'})
        }
        this.$emit('infoPopup', {status: response.data.status, msg: response.data.message})
      } else {
          this.$emit('infoPopup', {status: "danger", msg: "Something went wrong..."})
      }
    }
  }
}
</script>

<style scoped>
.jumbotron {
    margin-top: 15px;
}

.form-wrapper {
    width: 50%;
    margin: auto;
}

.input-grouped-2 input {
    width: 49%;
}

input {
    width: 100%;
    height: 30px;
    margin: 25px 2px;
    padding: 20px;
    font-size: medium;
    border-radius: 30px;
}

button {
    margin: 10px;
}
</style>