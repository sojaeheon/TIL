<template>
  <div class="child-card">
    <h3>자식 페이지입니다</h3>
    <p>이름: {{ child.name }}</p>
    <p>나이: {{ child.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
.child-card {
  border: 1px solid #616161;

  padding: 16px;
  background-color: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
</style>