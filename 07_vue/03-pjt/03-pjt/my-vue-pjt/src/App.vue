
<!--
루트 컴포넌트. 내비게이션 + router-view.
-->
<script setup>
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />
  <main class="container py-4">
    <router-view />
  </main>
</template>

<style>
body { margin: 0; font-family: 'Noto Sans KR', sans-serif; }
.container { max-width: 900px; margin: 0 auto; }
</style>
