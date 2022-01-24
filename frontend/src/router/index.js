import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Subject from '../views/Subject.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/subject/:id',
    name: 'Subject',
    component: Subject
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
