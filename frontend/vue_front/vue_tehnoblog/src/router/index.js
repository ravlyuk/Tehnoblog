import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Single from '../views/Single.vue'
import Rubric from '../views/Rubric.vue'


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/article/:id',
        name: 'Single',
        component: Single,
        props: true,
    },
    {
        path: '/rubric/:id',
        name: 'Rubric',
        component: Rubric,
        props: true,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
