<!--
상단 내비게이션. 4개 라우트 링크.
-->
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
    <div class="container">
      <router-link class="navbar-brand" to="/">영화정보</router-link>
      <div>
        <router-link class="nav-link" to="/movies">영화목록</router-link>
        <router-link class="nav-link" to="/review-search">리뷰검색</router-link>
      </div>
    </div>
  </nav>
</template>
<script setup></script>
<style scoped>
.nav-link { margin-right: 1rem; }
</style>
