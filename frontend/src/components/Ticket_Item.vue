<template>
    <div class="wrapper">
    {{ItemData.subject}}
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
        width: 100% !important
        height: 10vh !important
</style>
