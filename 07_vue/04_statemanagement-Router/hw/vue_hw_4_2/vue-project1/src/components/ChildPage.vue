<template>
  <div class="child-card">
    
    <h2>자식 페이지</h2>
    <p>{{ child.name }}</p>
    
  </div>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>
.child-card {
  background-color: #ffffff;
  border: 1px solid #eee;
  border-radius: 4px;
  padding: 10px;
  margin-top: 10px;
  text-align: center; 
}
.child-title {
  font-weight: bold;
  margin-bottom: 4px;
}
</style>