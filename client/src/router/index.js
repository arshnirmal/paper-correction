import Vue from "vue";
import VueRouter from "vue-router";
//import Home from "../views/Home.vue";
import home from "../components/home.vue";
import test from "../components/test.vue";
import final from "../components/final.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: home
  },
  {
    path: "/test",
    name: "test",
    component: test
  },
  {
    path: "/final",
    name: "final",
    component: final
  },
];

const router = new VueRouter({
  routes
});

export default router;
