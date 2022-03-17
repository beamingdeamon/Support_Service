<template>
	<div class="wrapper">
		<div class="content_wrapper">
			<h1>Registration</h1>
			<form >
        <input type="mail" v-model="email" class="inputs" placeholder="Enter your email" required>
        <input type="text" v-model="first_name" class="inputs" placeholder="Enter your firstname" required>
        <input type="text" v-model="last_name" class="inputs" placeholder="Enter your lastname" required>
        <input type="password" v-model="password" class="inputs" placeholder="Enter your password" required>
        <button class="send" @click="RegisterUser">Register</button>
      </form>
			<router-link :to='{ path: `/` }' class="login">Login</router-link>
		</div>
	</div>
</template>

<script>

export default {
	data() {
		return {
			first_name: null,
			last_name: null,
			email: null,
			password: null,
			role_id: 1,
			results: [],
		};
	},
	methods:{
		RegisterUser(){
			const requestOptions = {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({email: this.email, first_name: this.first_name,last_name: this.last_name,  password: this.password, role_id: this.role_id})
			};
			
			fetch("http://127.0.0.1:5000/api/register", requestOptions)
				.then(response => {this.results = response.data})
				.then(data => (this.postId = data.id));
		}
  },
}
</script>

<style lang="sass" scoped>
	header
		display: none !important
	.wrapper
		width: 100vw
		height: 100vh
		display: flex
		align-items: center
		justify-content: center
		background-color: #7e8c73
		.content_wrapper
			width: 30vw
			height: 60vh
			background-color: #adbf9f
			display: flex
			flex-direction: column
			align-items: center
			form
				display: flex
				flex-direction: column
				width: 100%
				height: 70%
				align-items: center
				justify-content: center
				.inputs
					width: 60%
					font-size: 2vh
					height: 3.5vh
					margin-top: 2vh
				.send
					margin-top: 2vh
					font-size: 2vh
					cursor: pointer
					margin-left: 50%
			.login
				text-decoration: none
				font-size: 2vh
				color: white
</style>
