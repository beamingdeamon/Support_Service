<template>
  <div>
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
export default {
  name:'App',
  components:{
    Header
  }
}
</script>

<style lang="sass">
body
  margin:0
</style>
