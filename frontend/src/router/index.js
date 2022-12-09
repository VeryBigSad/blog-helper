import { createRouter, createWebHashHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import("../views/HomeView.vue")
  },
  // path for blog post detail
  {
    path: '/blog/:id',
    name: 'blog',
    component: () => import("../views/BlogPostView.vue")
  },
  // path for blog post creation
  {
    path: '/blog/create',
    name: 'blog-create',
    component: () => import("../views/BlogPostCreateView.vue")
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router