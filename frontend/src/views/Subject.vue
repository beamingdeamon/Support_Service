<template>
  <div class="wrapper">
    <div class="main_wrapper">
      <div class="message_block">
        <Subject_Item class="subject_item"
          v-for="item in subject" 
          :key="item.id" 
          :ItemData = "item" />
      </div>
      <form >
        <input type="number" v-model="user_id" class="input_id" placeholder="Id" required>
        <input type="text" v-model="message" class="input_message" placeholder="message" required>
        <button class="send" @click="SendMessage">Send</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Subject_Item from '@/components/Subject_Item.vue'
export default {
	data() {
    return {
      subject: [],
      user_id: null,
      message: null,
      ticket_id: this.$route.params.id,
    };
	},
	components:{
	Subject_Item
},
  mounted() {
    axios
      .get('http://localhost:8000/api/getmessages/'+ this.ticket_id)
      .then(response => (this.subject = response.data));
  },
  methods:{
    SendMessage(){
      const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: this.user_id, message: this.message, ticket_id: this.ticket_id})
      };
      fetch("http://localhost:8000/api/createmessage/", requestOptions)
        .then(response => response.json())
        .then(data => (this.postId = data.id));
  }
}
}
</script>

<style lang="sass" scoped>
  .wrapper
    width: 100vw
    height: 80vh !important
    display: flex
    justify-content: center
    .main_wrapper
      width: 80%
      height: 100%
      border: 1px solid grey
      .input_id
        width: 2%
        height: 3.6vh
      .input_message
        width: 90%
        height: 3.6vh
      .send
        width: 7%
        height: 3.6vh
        color: #FA1451
        border: none
        font-family: GothamLight
        font-size: 2vh
        cursor: pointer
      input
        background-color: white
        border: 1px solid grey
        outline: none
        color: black
        font-size: 1.8vh
        text-align: center
      ::-webkit-input-placeholder
        color: grey
        font-size: 1.8vh
        font-family: GothamLight
        text-align: center
        transition: opacity .5s
        opacity: 1
      input:focus::-webkit-input-placeholder
        opacity: 0
      ::-moz-placeholder
        color: grey
        font-size: 1.8vh
        font-family: GothamLight
        text-align: center
        transition: opacity .5s
        opacity: 1
      input:focus::-moz-placeholder
        opacity: 0
      :-moz-placeholder
        color: grey
        font-size: 1.8vh
        font-family: GothamLight
        text-align: center
        transition: opacity .5s
        opacity: 1
      input:focus:-moz-placeholder
        opacity: 0
      :-ms-input-placeholder
        color: grey
        font-size: 1.8vh
        font-family: GothamLight
        text-align: center
        transition: opacity .5s
        opacity: 1
      input:focus:-ms-input-placeholder
        opacity: 0
      .message_block
        width: 100%
        height: 95%
        overflow: auto
        .subject_item
          margin-top: 2vh 
</style>
