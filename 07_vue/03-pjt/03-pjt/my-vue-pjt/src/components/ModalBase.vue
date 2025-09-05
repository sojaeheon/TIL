<!--
공용 모달. ESC 닫기, aria-label 지원.
-->
<template>
  <div v-if="show" class="modal-backdrop" @click.self="close" tabindex="-1" aria-label="모달" @keydown.esc="close">
    <div class="modal-content" role="dialog" aria-modal="true">
      <slot />
      <button class="btn btn-secondary mt-2" @click="close" aria-label="닫기">닫기</button>
    </div>
  </div>
</template>
<script setup>
import { onMounted, onUnmounted } from 'vue'
const props = defineProps({ show: Boolean })
const emit = defineEmits(['close'])
function close() { emit('close') }
function handleKey(e) { if (e.key === 'Escape') close() }
onMounted(() => window.addEventListener('keydown', handleKey))
onUnmounted(() => window.removeEventListener('keydown', handleKey))
</script>
<style scoped>
.modal-backdrop {
  position: fixed; top:0; left:0; width:100vw; height:100vh;
  background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; z-index: 1000;
}
.modal-content {
  background: #fff; padding: 2rem; border-radius: 8px; min-width: 320px; max-width: 90vw;
}
</style>
