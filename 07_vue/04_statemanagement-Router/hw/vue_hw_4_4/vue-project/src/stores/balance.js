import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useBalanceStore = defineStore('balance', () => {
  // state
  const balances = ref([
    { name: '김하나', balance: 100000 },
    { name: '김두리', balance: 10000 },
    { name: '김서이', balance: 100 },
  ])

  // getters
  const getByName = (name) => {
    return balances.value.find(item => item.name === name)
  }

  // actions
  const updateBalance = (name, amount) => {
    const target = balances.value.find(item => item.name === name)
    if (target) {
      target.balance += amount
    }
  }

  return {
    balances,
    getByName,
    updateBalance
  }
})