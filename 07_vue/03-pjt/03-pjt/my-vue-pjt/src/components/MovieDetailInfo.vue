<!--
영화 상세 정보. 제목/개봉일/평점/장르/줄거리.
-->
<template>
  <div class="detail-wrap">
    <img v-if="movie.poster_path" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="detail-poster" :alt="movie.title" />
    <div class="detail-info">
      <h2>{{ movie.title }}</h2>
      <div class="detail-meta">
        <span>개봉일: {{ movie.release_date }}</span>
        <span>평점: <span class="score">⭐ {{ movie.vote_average }}</span></span>
        <span>장르: {{ genreNames }}</span>
      </div>
      <p class="detail-overview">{{ movie.overview }}</p>
    </div>
  </div>
</template>
<script setup>
const props = defineProps({ movie: Object })
const genreNames = props.movie.genres?.map(g => g.name).join(', ') || ''
</script>

<style scoped>
.detail-wrap {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 16px rgba(44,62,80,0.08);
  padding: 2rem;
  margin-bottom: 2rem;
}
.detail-poster {
  width: 220px;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(44,62,80,0.10);
  object-fit: cover;
}
.detail-info {
  flex: 1;
}
.detail-meta {
  display: flex;
  gap: 1.5rem;
  font-size: 1.05rem;
  margin-bottom: 1rem;
  color: #666;
}
.score {
  color: #ff4f6e;
  font-weight: 700;
}
.detail-overview {
  margin-top: 1.2rem;
  font-size: 1.08rem;
  line-height: 1.7;
  color: #333;
}
@media (max-width: 700px) {
  .detail-wrap {
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
  }
  .detail-poster {
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
  }
}
</style>
