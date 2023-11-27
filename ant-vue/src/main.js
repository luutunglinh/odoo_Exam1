import { createApp } from 'vue'
import App from './App.vue'
import vueRouter from './router/index.js'
import Antd from 'ant-design-vue'
import MToast from './components/base/MToast.vue'
const app = createApp(App)
app.component(MToast)
app.use(vueRouter)
app.use(Antd)
app.mount('#app')
