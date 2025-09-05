<template>
  <div>
    <p>이름 : {{ person.name }}</p>
    <p>잔고 : {{ person.balance }}</p>
    <button @click="goToUpdate(person.name)">updateBalance</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  person: Object
})

const router = useRouter()

const goToUpdate = (name) => {
  router.push({ name: 'update', params: { name } })
}

</script>

<style scoped>

</style>