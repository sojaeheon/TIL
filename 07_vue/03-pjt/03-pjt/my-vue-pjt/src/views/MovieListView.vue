<!--
TMDB Top Rated 영화 목록. 카드 그리드.
-->
<template>
  <div>
    <h2>Top Rated 영화</h2>
    <div v-if="loading">로딩 중...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else class="row row-cols-2 g-4">
      <div v-for="movie in movies" :key="movie.id" class="col">
        <MovieCard :movie="movie" />
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { fetchTopRatedMovies } from '../services/tmdb'
import MovieCard from '../components/MovieCard.vue'

const movies = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    movies.value = await fetchTopRatedMovies()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>
