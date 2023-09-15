import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/Home.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/colors',
    name: 'colors',
    component: () => import('../views/Colors.vue'),
    async beforeEnter(to, from, next) {
      try {
        var hasPermission = localStorage.getItem("hasPermission");
        if (hasPermission) {
          next()
        }
        else {
          next({
            name: "login"
          })
        }
      } catch (e) {
        next({
          name: "login"
        })
      }
    } 
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/reset',
    name: 'reset',
    component: () => import('../views/Reset.vue')
  },
  {
    path: '/reset/password',
    name: 'reset-password',
    component: () => import('../views/ResetPassword.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
