<template>
  <div>
    <h1>부모 페이지</h1>
    <ChildPage 
      v-for="(child, index) in children" 
      :key="index" 
      :child="child"
      @giveMeAllowance="updateBalance"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30, balance: 100000 },
  { name: '김두리', age: 20, balance: 10000 },
  { name: '김서이', age: 10, balance: 10002 }
])

// 자식이 요청하면 해당 balance + 1000
const updateBalance = (child) => {
  child.balance += 1000
}
</script>
