//Imporing libraries

import { createApp, VueElement} from 'vue'
import App from './App.vue'
import router from './router'
import { plugin, defaultConfig } from '@formkit/vue'
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";

import axios from 'axios';


//Linking our backend.
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5001/';  


//Initializing our web application
const app = createApp(App)

app.use(router, plugin, defaultConfig, VueElement, useValidate, required)

app.mount('#app')
