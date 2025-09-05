import {ref,computed} from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('article', () => {
  const article = ref()
  

  return { article }
})
