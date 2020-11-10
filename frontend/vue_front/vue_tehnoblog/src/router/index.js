import Vue from 'vue'
import VueRouter from 'vue-router'
import Single from '../views/Single.vue'
import List from '../views/List.vue'
import About from '../views/About.vue'


Vue.use(VueRouter)

export const routes = [
    {
        path: '/',
        name: 'Home',
        component: List
    },
    {
        path: '/article/:id',
        name: 'Single',
        component: Single,
        props: true,
    },
    {
        path: '/rubric/:id',
        name: 'List',
        component: List,
        props: true,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/services',
        name: 'Services',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Services.vue')
    },
    {
        path: '/contacts',
        name: 'Contacts',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/Contacts.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
