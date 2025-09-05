<template>
  <div class="parent-container" >
    <h1>부모 페이지입니다</h1>
    <Childpage v-for="(child, index) in children" 
      :key="index" 
      :child="child" 
      />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Childpage from './Childpage.vue';

const children = ref([
  { name : '김하나', age : 30},
  { name : '김두리', age : 20},
  { name : '김서이', age : 10},
])

</script>

<style scoped>
.parent-container {
  padding: 20px;
  border: 2px solid #616161;
}

</style>