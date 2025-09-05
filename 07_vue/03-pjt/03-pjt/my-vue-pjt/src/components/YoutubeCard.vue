<!--
YouTube 영상 카드. 썸네일/제목/채널명.
-->
<template>
  <div class="card h-100" @click="onClick" style="cursor:pointer">
    <img :src="video.snippet.thumbnails.medium.url" class="card-img-top" :alt="video.snippet.title" />
    <div class="card-body">
      <h6 class="card-title">{{ video.snippet.title }}</h6>
      <p class="card-text">{{ video.snippet.channelTitle }}</p>
    </div>
  </div>
</template>
<script setup>
const props = defineProps({ video: Object })
const emit = defineEmits(['select'])
function onClick() { emit('select', props.video) }
</script>
