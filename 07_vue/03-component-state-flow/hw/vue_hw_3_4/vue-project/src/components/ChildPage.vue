<template>
  <div class="child-card">
    <p>이름: {{ child.name }}</p>
    <p>나이: {{ child.age }}</p>
    <p>용돈: {{ child.balance }} 원</p>
    <button @click="$emit('giveMeAllowance', child)">용돈 더 주세요</button>
  </div>
</template>

<script setup>
defineProps({
  child: Object
})
</script>

<style scoped>
.child-card {
  border: 1px solid #ccc;
  margin: 8px;
  padding: 12px;
  border-radius: 8px;
}
button {
  margin-top: 6px;
  padding: 6px 12px;
  cursor: pointer;
}
</style>
