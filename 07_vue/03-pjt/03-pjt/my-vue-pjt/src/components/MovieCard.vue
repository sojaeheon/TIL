<!--
영화 카드. 포스터/제목/평점. 클릭 시 상세 이동.
-->
<template>
  <div class="movie-card card h-100" @click="goDetail" tabindex="0" aria-label="영화 상세 보기">
    <img :src="posterUrl" class="card-img-top" :alt="movie.title" />
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">⭐ {{ movie.vote_average }}</p>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps({ movie: Object })
const router = useRouter()
const posterUrl = props.movie.poster_path
  ? `https://image.tmdb.org/t/p/w500${props.movie.poster_path}`
  : 'https://via.placeholder.com/300x450?text=No+Image'
function goDetail() {
  router.push(`/movies/${props.movie.id}`)
}
</script>

<style scoped>
/* .movie-card {
  transition: transform 0.18s, box-shadow 0.18s;
  box-shadow: 0 2px 12px rgba(44,62,80,0.08);
}
.movie-card:hover, .movie-card:focus {
  transform: translateY(-6px) scale(1.03);
  box-shadow: 0 8px 32px rgba(44,62,80,0.18);
  outline: none;
}
.card-title {
  font-size: 1.08rem;
  font-weight: 700;
  color: #2c3e50;
}
.card-text {
  color: #4f8cff;
  font-weight: 600;
} */
</style>
