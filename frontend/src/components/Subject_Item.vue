<template>
  <div class="message_wrapper">
    <div class="user_id_wrapper">{{ItemData.user_id}}</div>
    <div class="message_wrapper">{{ItemData.message}}</div>
    <div class="message_date_wrapper">{{ItemData.created_date}}</div>
  </div>
</template>

<script>
export default {
    name: 'SubjectItem',
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
  .message_wrapper
    height: 5vh
    width: 100%
    display: flex
    flex-direction: row
    border-top: 1px solid grey
    border-bottom: 1px solid grey
    .user_id_wrapper
      width: 2.5%
      font-size: 2.5vh
      text-align: center
      border-right: 1px solid grey
    .message_wrapper
      width: 90%
      font-size: 2vh
      color: #5dcbde
      border-right: 1px solid grey

</style>
