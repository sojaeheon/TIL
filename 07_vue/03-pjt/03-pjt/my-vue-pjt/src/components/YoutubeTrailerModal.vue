<!--
영화 예고편 모달. YouTube embed.
-->
<template>
  <ModalBase :show="show" @close="onClose">
    <div v-if="videoId">
      <iframe
        :src="`https://www.youtube.com/embed/${videoId}`"
        width="400" height="225"
        frameborder="0" allowfullscreen
        aria-label="예고편 영상"
      ></iframe>
    </div>
    <div v-else>예고편 영상을 찾을 수 없습니다.</div>
  </ModalBase>
</template>
<script setup>
import ModalBase from './ModalBase.vue'
const props = defineProps({ show: Boolean, videoId: String })
const emit = defineEmits(['close'])
function onClose() { emit('close') }
</script>
