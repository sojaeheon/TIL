<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <div v-if="target">
      <p>이름: {{ target.name }}</p>
      <p>잔고: {{ target.balance }} 원</p>
      <button @click="increaseBalance">+</button>
    </div>
    <div v-else>
      <p>해당 사용자를 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>

import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const balanceStore = useBalanceStore()

const target = balanceStore.getByName(route.params.name)

const increaseBalance = () => {
  balanceStore.updateBalance(route.params.name, 1000)
}
</script>

<style scoped>

</style>