import { createApp, VueElement} from 'vue'
import App from './App.vue'
import router from './router'
import { plugin, defaultConfig } from '@formkit/vue'
import useValidate from "@vuelidate/core";
import { required } from "@vuelidate/validators";

const app = createApp(App)

app.use(router, plugin, defaultConfig, VueElement, useValidate, required)

app.mount('#app')
