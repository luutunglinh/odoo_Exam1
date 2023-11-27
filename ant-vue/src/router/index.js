import { createRouter, createWebHashHistory } from 'vue-router'
import TheDashboard from '../components/view/TheDashboard.vue'
import TheStore from '../components/view/TheStore.vue'
import TheInstallation from '@/components/view/TheInstallation.vue'
import TheCustomize from '@/components/view/TheCustomize.vue'
const routes = [
  {
    path: '/',
    component: TheDashboard,
    name: 'dashboard'
  },
  {
    path: '/dashboard/thestore/:id',
    component: TheStore,
    name: 'thestore'
  },
  {
    path: '/installation',
    component: TheInstallation,
    name: 'theinstallation'
  },
  {
    path: '/customize',
    component: TheCustomize,
    name: 'thecustomize'
  }

]

const vueRouter = createRouter({
  history: createWebHashHistory(),
  routes,
  linkActiveClass: 'active',
  linkExactActiveClass: 'exact-active'
})

export default vueRouter
