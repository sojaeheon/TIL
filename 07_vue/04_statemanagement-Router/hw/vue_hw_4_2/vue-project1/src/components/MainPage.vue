<template>
  <div class="main-container">
    <h1>Pinia 연습하기</h1>
    <ParentPage
      v-for="(family, index) in familyStore.familyInfo"
      :key="index"
      :family="family"
    />
  </div>
</template>

<script setup>
import { useFamilyStore } from '@/stores/family'
import ParentPage from './ParentPage.vue';

const familyStore = useFamilyStore()
console.log(familyStore)
</script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>