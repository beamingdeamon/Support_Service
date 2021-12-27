<template>
	<div class="wrapper">
		<div class="content_wrapper">
			<div class="support_subjects">
				Support Subjects
			</div>
			<div class="ticket_item" v-for="item in ticket" 
			:key="item.id" 
			:ticket_data = "item">
				{{ticket_data.subject}}
				2021-12-21
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
    return {
      ticket: []
    };
	},
  mounted() {
    axios
      .get('http://localhost:8000/api/gettickets/')
      .then(response => (this.ticket = response.data));
  }
}
</script>

<style lang="sass" scoped>
	.wrapper
		width: 100vw
		height: 86vh
		display: flex
		align-items: center
		justify-content: center
		.content_wrapper
			width: 80%
			height: 100%
			.support_subjects
				margin-top: 3vh
				font-size: 5vh
				margin-left: 5vh
			.ticket_item
				margin-top: 2vh
				font-size: 4vh
</style>
