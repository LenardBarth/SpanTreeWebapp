import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/router.js";
import './axios.js';

createApp(App).use(router).mount("#app");
