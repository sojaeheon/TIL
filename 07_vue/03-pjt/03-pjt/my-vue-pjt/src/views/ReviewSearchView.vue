<!--
리뷰 영상 검색/모달 재생. 키워드 입력 → 카드 리스트.
-->
<template>
  <div>
    <h2>영화 리뷰 영상 검색</h2>
    <form @submit.prevent="search">
      <input v-model="keyword" placeholder="영화 제목 입력" class="form-control" />
      <button class="btn btn-primary mt-2" :disabled="loading">검색</button>
    </form>
    <div v-if="loading">로딩 중...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else class="row row-cols-2 row-cols-md-3 g-4 mt-3">
      <div v-for="video in videos" :key="video.id.videoId" class="col">
        <YoutubeCard :video="video" @select="openModal" />
      </div>
    </div>
    <YoutubeReviewModal :show="showModal" :videoId="selectedId" @close="showModal=false" />
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { searchYoutubeVideos } from '../services/youtube'
import YoutubeCard from '../components/YoutubeCard.vue'
import YoutubeReviewModal from '../components/YoutubeReviewModal.vue'

const keyword = ref('')
const videos = ref([])
const loading = ref(false)
const error = ref('')
const showModal = ref(false)
const selectedId = ref('')

async function search() {
  if (!keyword.value.trim()) return
  loading.value = true
  error.value = ''
  try {
    const q = `${keyword.value} 리뷰`
    videos.value = await searchYoutubeVideos(q)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

function openModal(video) {
  selectedId.value = video.id.videoId
  showModal.value = true
}
</script>
