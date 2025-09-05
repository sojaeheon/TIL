<template>
  <div>
    <h1>About View</h1>
    <button @click = "someFunction">엄청 복잡한 무언가</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

const someFunction = function(){
  router.push({ name :'userProfile',params:{'username':'admin'}})
}


</script>

<style scoped>

</style>