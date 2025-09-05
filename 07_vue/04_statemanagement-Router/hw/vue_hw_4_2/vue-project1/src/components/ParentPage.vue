<template>
  <div class="parent-card">
   <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>

    <ChildPage
      v-for="(child, index) in family.children"
      :key="index"
      :child="child"
    />
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue'

defineProps({
  family: Object
})
</script>

<style scoped>
.parent-card {
  background-color: #fafafa;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 20px;
  text-align: center; 
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.parent-title {
  font-weight: bold;
  margin-bottom: 10px;
}

.parent-info {
  margin: 0;
  padding: 0;
  list-style: none;
}

.parent-info li {
  margin-bottom: 4px;
}
</style>