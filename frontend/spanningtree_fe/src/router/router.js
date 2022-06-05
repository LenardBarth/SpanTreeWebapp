import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home";
import Login from "@/views/Login";
import Register from "@/views/Signup";
import Result from "@/views/Result";
import Projects from "@/views/Projects";

// Defines rotes at which certain components are rendered
// works via <router-view> which will be replaced by component at each route respectfully
const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/result",
    name: "Result",
    component: Result,
  },
  {
    path: "/projects",
    name: "Projects",
    component: Projects,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
