<template>
    <div class="wrapper">
		<div class="links">
			<router-link :to='{ path: `/` }' class="Link"> Support </router-link>
			<router-link :to='{ path: `/` }' class="Link"> Support </router-link>
			<router-link :to='{ path: `/` }' class="Link"> Support </router-link>
			<router-link :to='{ path: `/` }' class="Link"> Support </router-link>
		</div>
    </div>
</template>

<style lang="sass" scoped>
	.wrapper
		height: 7vh
		width: 100%
		background-color: grey
		.links
			margin-left: 30vw
			width: 70vw
			height: 100%
			display: flex
			flex-direction: row
			align-items: center
			justify-content: space-around
			float: left
			.Link
				color: black
				font-size: 2vh
				text-decoration: none
</style>
