import { createRouter, createWebHistory } from 'vue-router'


import HomeView from '../views/HomeView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ReviewSearchView from '../views/ReviewSearchView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/movies', component: MovieListView },
  { path: '/movies/:movieId', component: MovieDetailView, props: true },
  { path: '/review-search', component: ReviewSearchView },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
