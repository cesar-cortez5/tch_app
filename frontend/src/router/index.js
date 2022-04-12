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
      component: () => import('../views/NewCustomer.vue')
    },
    {
      path: '/returning_customer',
      name: 'returning_customer',
      component: () => import('../views/ReturningCustomer.vue')
    },
    {
      path: '/customer_query_id:customerId',
      redirect: to => {
        return {path: 'customer_query_id', query: {'customer_id': to.params.customerId}}
      }
    
    },
    {
      path: '/customer_query_id',
      name: 'customer_query',
      component: () => import ('../views/Customer.vue')
    },
    {
      /* This is used whenever search is made for a name. For instance, if a customer searches for cesar cortez,
      the link will be /customer_query?customerName=cesar%cortez, but it will redirect to /customer_query, and send 
      'cesar cortez' as a parameter    
      */
      path: '/customer_query:customerName',
      redirect: to => {
        return { path: '/customer_query', query: { 'customer_name': to.params.customerName } }
      }
    },
    {
      path: '/customer_query',
      name: 'customer_query',
      component: () => import('../views/CustomersSearchResult.vue'),

    }, //Add your new router here. Make sure you add the component: ()=> import('') statement as this is what imports your webpage.  
    {
      path: '/customer_query',
      name: 'customer_query',
      component: () => import('../views/CustomersSearchResult.vue'),

    } //Add your new router here. Make sure you add the component: ()=> import('') statement as this is what imports your webpage.  

  ]
})

export default router
