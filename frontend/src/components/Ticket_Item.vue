<template>
    <div class="wrapper">
      <div class="link_wrapper">
        <router-link :to='{ path: `/subject/${ ItemData.id }` }' class="Link">{{ItemData.subject}}</router-link>
      </div>
      <div class="date_wrapper">
        <div class="date">
          {{ItemData.date}}
        </div>
      </div>
        
    </div>
</template>

<script>
export default {
    name: 'TicketItem',
    data: () => ({
    }),
    props: {
        ItemData: {
            type: Object,
            default: () => {}
        }
    }
}
</script>

<style lang="sass" scoped>
  .wrapper
    width: 80vw !important
    height: 10vh !important
    border-top: 1px solid grey
    border-bottom: 1px solid grey
    .date_wrapper
      width: 50%
      height: 100%
      .date
        margin-left: 28vw
        font-size: 3vh
    .link_wrapper
      width: 50%
      height: 100%
      display: flex
      align-items: center
      .Link
        margin-left: 2vw
        color: black
        text-decoration: none
</style>
