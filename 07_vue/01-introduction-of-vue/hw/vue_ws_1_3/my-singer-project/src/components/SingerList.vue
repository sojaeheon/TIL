<template>
  <div>
    <h1>가수 목록</h1>
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from './singers/SingerDetail.vue';


</script>

<style scoped>
h1 {
  display: flex;
  flex-direction: column;
  align-items: center;

}
</style>