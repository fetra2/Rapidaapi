import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons'

//import 'bootstrap/dist/css/bootstrap.css' //see App.vue
import 'animate.css'

library.add(faShoppingCart)

createApp(App).use(router).component('fa', FontAwesomeIcon).mount('#app')