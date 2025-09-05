<!--
영화 상세. 정보 + 예고편 버튼/모달.
-->
<template>
  <div>
    <div v-if="loading">로딩 중...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <MovieDetailInfo :movie="movie" />
      <button class="btn btn-danger mt-3" @click="openTrailer">공식 예고편 보기</button>
      <YoutubeTrailerModal :show="showModal" :videoId="trailerId" @close="showModal=false" />
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { fetchMovieDetail } from '../services/tmdb'
import { searchYoutubeVideos } from '../services/youtube'
import MovieDetailInfo from '../components/MovieDetailInfo.vue'
import YoutubeTrailerModal from '../components/YoutubeTrailerModal.vue'

const route = useRoute()
const movie = ref(null)
const loading = ref(true)
const error = ref('')
const showModal = ref(false)
const trailerId = ref('')

onMounted(async () => {
  try {
    movie.value = await fetchMovieDetail(route.params.movieId)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})

async function openTrailer() {
  showModal.value = true
  try {
    const q = `${movie.value.title} 공식 예고편`
    const videos = await searchYoutubeVideos(q, 1)
    trailerId.value = videos[0]?.id?.videoId || ''
  } catch {
    trailerId.value = ''
  }
}
</script>
