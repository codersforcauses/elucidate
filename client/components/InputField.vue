<template>
  <div>
    <label>{{fieldName}}</label>
    <div class="flex items-center">
      <ValidationProvider :rules="rules" v-slot="{ errors }" class="w-full">
        <input v-if="isPassword && !showText" :name ="fieldName" type="password" class="w-full h-10 drop-shadow-lg my-3 px-2" :value="inputvalue" @input="$emit('update:inputvalue', $event.target.value)">
        <input v-else type="fieldType" :name ="fieldName" class="w-full h-10 drop-shadow-lg my-3 px-2" :value="inputvalue" @input="$emit('update:inputvalue', $event.target.value)">
        <span class="text-red">{{ errors[0] }}</span>
      </ValidationProvider>
      <button type="button" v-if="isPassword" v-on:click="clickCheck" class="text-center h-10 px-1 mx-1 bg-white border-2 border-green2 rounded">SHOW</button>
    </div>
  </div>
</template>

<!-- <script src="./Validator.js"></script> -->

<script>
// Validation
// ---------------------------------------
import { ValidationProvider, extend } from 'vee-validate';
import { required, email } from 'vee-validate/dist/rules';

extend('email',{ 
  ...email,
  message:'Invalid email address'

});

extend('required',{
  ...required,
  message:'This field is required'
});

extend('password', {
  params: ['target'],
  validate(value, { target }) {
    console.log(target)
    return value === target;
  },
  message: 'Password confirmation does not match'
});


// ---------------------------------------
  export default {
    name: 'InputField',
    components: {
    ValidationProvider
    },
    data: () => ({
      showText: false,
      test: "test"
    }),
    props: {
      fieldName: String,
      fieldType: String,
      isPassword: Boolean,
      rules: String,
      inputvalue: String
    },
    methods: {
      clickCheck: function() {
        this.showText = !this.showText
        console.log(this.value)
      }
    }
  }
</script>