<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader :pageTitle="title" />

    <div class="flex flex-grow justify-center">
      <TealBox>
        <ValidationObserver v-slot="{ invalid }" class="w-full">
          <form @submit.prevent="onSubmit" class="flex flex-col w-11/12 mx-6 my-8">
            <InputField  v-for="field in fields" 
            :key="field.index" 
            :fieldName="field.name" 
            :fieldType="field.type" 
            :isPassword="field.isPassword"
            :rules="field.rules"
            :inputvalue.sync="field.value"
            :id = "field.id" />
          <button type="submit" :class="invalid ? 'text-darkgrey bg-lightgrey':'text-red bg-white'" class="place-self-center text-l font-bold drop-shadow-lg w-24 h-8 rounded border border-solid mt-5">Submit</button>
          <!-- <button v-else type="submit" :disabled="invalid" class="place-self-center text-l font-bold text-red bg-white w-24 h-8 rounded border border-solid mt-5">Submit</button> -->
          </form>
        </ValidationObserver>
      </TealBox>

    </div>
    <AuthFooter />
  </div>
</template>

<script>
import {ValidationObserver} from 'vee-validate';

let count = 0;
export default{
  name: 'signup-page',
  components: {
    ValidationObserver,
  },
  data: () => ({
    title: "Sign-Up",
    password:'',
    confirm : '',
    ispassword: true,
    btnDisable: true,
    fields: [
      { name: "First Name", type: "text", isPassword: false, index: count++, id:"firstname", rules:"required" },
      { name: "Last Name", type: "text", isPassword: false, index: count++, id:"lastname", rules:"required" },
      { name: "Email", type: "text", isPassword: false, index: count++, id:"email", rules:"required|email"},
      { name: "Password", type: "text", isPassword: true, index: count++, id:"password", rules:"required|min:6"},
      { name: "Password Confirmation", type: "text", isPassword: true, index: count++, id:"confirm", rules:"required|password:@password" },
      { name: "Grade", type: "text", isPassword: false, index: count++, id:"grade", rules:"required" }, 
    ]
  }),
  methods: {
    onSubmit () {
      alert('Form has been submitted!');
    }
  }
};
</script>
