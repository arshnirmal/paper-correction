import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import PictureInput from 'vue-picture-input';
import VueProgressBar from 'vue-progressbar';
import VueSocketIO from 'vue-socket.io';


const VueUploadComponent = require('vue-upload-component')
Vue.component('file-upload', VueUploadComponent)
const options = {
  color: '#bffaf3',
  failedColor: '#874b4b',
  thickness: '2px',
  transition: {
    speed: '0.2s',
    opacity: '0.6s',
    termination: 300
  },
  autoRevert: true,
  location: 'top',
  inverse: false
}

Vue.use(VueProgressBar, options)
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://127.0.0.1:5000',
    vuex: {
        store,
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
    },
}))



Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.config.productionTip = false;
// register globally
Vue.component('picture-input', PictureInput)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
