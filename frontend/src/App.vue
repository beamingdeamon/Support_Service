<template>
  <div>
    <router-view
			:JwtData = "jwt"
    />
  </div>
</template>

<script>
export default {
  name:'App',
  data: () => ({
    jwt: null
    }),
}
</script>

<style lang="sass">
body
  margin:0
</style>
