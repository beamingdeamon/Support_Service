<template>
	<div class="wrapper">
		<div class="content_wrapper">
			<h1>Login</h1>
			<form >
        <input type="text" v-model="email" class="inputs" placeholder="Enter your email" required>
        <input type="password" v-model="password" class="inputs" placeholder="Enter your password" required>
        <button class="send" @click="LoginUser">Login</button>
      </form>
			<router-link :to='{ path: `/register` }' class="register">Registration</router-link>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			email: null,
			password: null,
			results:[]
		};
	},props: {
        JwtData: {
            type: Object,
            default: () => {}
        }
    },
	methods:{
		async LoginUser(){
			const response = await axios.post("http://127.0.0.1:5000/api/login", {
				email: this.email,
				password: this.password,
			});
			//localStorage.setItem("token", response.data.jwt);
			const status = JSON.parse(response.data.response.status);
			if (status == "200") {
				this.$router.push("/subjects");
			} else {
				alert("Bad")
			}
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
			.register
				text-decoration: none
				font-size: 2vh
				color: white

</style>
