<template>
    <!-- Source of Boostrap Alert Icons: https://getbootstrap.com/docs/5.0/components/alerts/ -->
    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
    <symbol id="check-circle-fill" fill="currentColor" viewBox="0 0 16 16">
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
    </symbol>
    <symbol id="info-fill" fill="currentColor" viewBox="0 0 16 16">
        <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
    </symbol>
    <symbol id="exclamation-triangle-fill" fill="currentColor" viewBox="0 0 16 16">
        <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
    </symbol>
    </svg>
    <div class="info-wrapper" v-if="this.showInfo">
        <div class="alert d-flex align-items-center alert-dismissible fade show" :class="alertStatus">
            <svg v-if="info.status=='info'" class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#info-fill"/></svg>
            <svg v-if="info.status=='success'" class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:"><use xlink:href="#check-circle-fill"/></svg>
            <svg v-if="info.status=='warning'" class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Warning:"><use xlink:href="#exclamation-triangle-fill"/></svg>
            <svg v-if="info.status=='danger'" class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
            <span>{{ info.msg }}</span>
        </div>
    </div>
</template>

<script>
export default {
  name: "userInfoPopup",
  props: ['info'],
  created() {
    // every time this component is created sets timer to hide component after
      this.customTimeout()
  },
  data() {
      return {
          alertStatus: "alert-" + this.info.status,
          showInfo: false,
      }
  },
  methods: {
      // after 2.45 seconds this component will not be displayed anymore
      customTimeout() {
        this.showInfo = true
        setTimeout(() => {
            this.showInfo = false
        }, 2450)
      }
  }
}
</script>

<style scoped>
.info-wrapper {
  max-width: 40vw;
  min-width: 25vw;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  margin: 25px 0;
  padding: 15px 30px;
  border-radius: 10px;
  color: #222222ba;
}
</style>