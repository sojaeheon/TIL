<template>
  <div class = "main-container">
    <h1>가수 정보 페이지에 오신 것을 환영합니다</h1>
    <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요.</p>
    <img src="../assets/microphone.jpg" class="microphone"></img>
  </div>
</template>

<script setup>
</script>

<style scoped>

.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  min-height: 100vh;
  padding: 40px;
  text-align: center;
}
.microphone {
  width: 200px;
  border-radius: 10px;
  margin-top: 20px;
}
</style>