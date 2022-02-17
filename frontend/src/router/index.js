import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Subject from '../views/Subject.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const routes = [
  {
    path: '/register',
    name: 'Registeration',
    component: Register
  },
  {
    path: '/',
    name: 'Authorization',
    component: Login
  },
  {
    path: '/subjects',
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
