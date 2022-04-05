import { createRouter, createWebHistory } from 'vue-router'

//To add a new router, add this to the end of the file
/*
    ,
    {
      path: '/REPLACE_THIS_WITH_YOUR_PAGE_NAME',
      name: 'REPLACE_THIS_WITH_YOUR_PAGE_NAME',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/NewCustomer.vue')
    }
*/

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/new_customer',
      name: 'new_customer',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/NewCustomer.vue')
    },
    {
      path: '/returning_customer',
      name: 'returning_customer',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ReturningCustomer.vue')
    },
    {    
      path: '/customer_query:customerName',
      redirect: to => {
        return {path: '/customer_query', query: {'customer_name': to.params.customerName}}
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
    }
  },
  {
    path: '/customer_query',
    name: 'customer_query',
    component: () => import('../views/Customers.vue'),

  } //Add your new router here
  ]
})

export default router
