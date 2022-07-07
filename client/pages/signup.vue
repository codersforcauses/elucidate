<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader :pageTitle="title" />

    <div class="flex flex-grow justify-center">
      <!-- Add sign up form here? -->
      <TealBox>
        <form class="flex flex-col w-11/12 mx-6 my-8">
          <ValidationObserver>
          <InputField  v-for="field in fields" 
          :key="field.index" 
          :fieldName="field.name" 
          :fieldType="field.type" 
          :isPassword="field.isPassword"
          :rules="field.rules"
          :inputvalue.sync="field.value" />
          </ValidationObserver>
          
        </form>
        <button v-on:click="printthis()">Click</button>
        <p>data is {{fields[0]["value"]}}</p>
        <p class="self-end mx-1 mb-1 mt-auto text-white drop-shadow-lg">Continue -></p>    
      </TealBox>

    </div>
    <AuthFooter />
  </div>
</template>

<script>
import {  ValidationObserver } from 'vee-validate';

let count = 0;
export default{
  name: 'signup-page',
  components: {
    ValidationObserver,
  },
  data: () => ({
    title: "Sign-Up",
    fields: [
      { name: "First Name", type: "text", isPassword: false, index: count++,rules:"required",value:"hi" },
      { name: "Last Name", type: "text", isPassword: false, index: count++,rules:"required",value:"" },
      { name: "Email", type: "text", isPassword: false, index: count++,rules:"required|email",value:"" },
      { name: "Password", type: "text", isPassword: true, index: count++,rules:"required|password:@confirm",value:"" },
      { name: "confirm", type: "text", isPassword: true, index: count++,rules:"required",value:"" },
      { name: "Grade", type: "text", isPassword: false, index: count++,rules:"required",value:"" }, 
    ]
  }),
  methods: {
    printthis:function (){
      console.log(this.fields[0].value)
    }
  },
};
</script>
