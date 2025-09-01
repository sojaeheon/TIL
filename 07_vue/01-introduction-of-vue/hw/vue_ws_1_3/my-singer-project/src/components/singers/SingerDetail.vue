<template>
  <div class="main-container">
    <h1>가수 이름</h1>
    <img src="../../assets/singer.jpg" alt="가수 이미지" class="singer">
    <p>가수 소개글</p>
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
  padding: 40px;
  text-align: center;
  border: 1px solid #000; /* 카드 테두리 */


}

.singer{
  width: 200px;
  height: 200px;
  border-radius: 50%; /* 원형 이미지 */
  object-fit: cover;  /* 이미지가 잘려도 비율 유지 */
  margin: 20px 0;
  border: 2px solid #333;
}
</style>