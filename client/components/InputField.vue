<template>
  <div>
    <label>{{fieldName}}</label>
    <div class="relative flex items-center">
      <input v-if="isPassword && !showText" type="password" class="w-full h-10 drop-shadow-lg my-3 px-2" v-model="inputValue">
      <input v-else type="fieldType" class="w-full h-10 drop-shadow-lg my-3 px-2" v-model="inputValue">
      <!-- <button type="button" v-if="isPassword" v-on:click="clickCheck" class="text-center h-10 px-1 mx-1 bg-white border-2 border-green2 rounded">SHOW</button> -->
      <img v-if="isPassword" @mouseover="clickCheck" @mouseleave="clickCheck" class="w-6 mx-2 absolute top-auto bottom-auto left-auto right-0" src="~/assets/eye.svg" />
    </div>
  </div>
</template>

<script>
  export default {
    name: 'InputField',
    data: () => ({
      showText: false,
      inputValue: "",
    }),
    props: {
      fieldName: String,
      fieldType: String,
      isPassword: Boolean,
    },
    methods: {
      clickCheck: function() {
        this.showText = !this.showText
        console.log(this.inputValue)
      }
    }
  }
</script>