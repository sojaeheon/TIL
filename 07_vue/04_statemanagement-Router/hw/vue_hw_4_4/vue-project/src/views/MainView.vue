<!-- src/views/MainView.vue -->
<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage 
      v-for="(person, index) in balanceStore.balances" 
      :key="index" 
      :person="person" 
    />
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance'
import MainPage from '@/components/MainPage.vue'

const balanceStore = useBalanceStore()
</script>
