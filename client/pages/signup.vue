<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader :pageTitle="title" />

    <div class="flex flex-grow justify-center">
      <TealBox>
        <ValidationObserver class="w-full">
        <form class="flex flex-col w-11/12 mx-6 my-8">
          <InputField  v-for="field in fields" 
          :key="field.index" 
          :fieldName="field.name" 
          :fieldType="field.type" 
          :isPassword="field.isPassword"
          :rules="field.rules"
          :inputvalue.sync="field.value"
          :id = "field.id" />
        </form>
         </ValidationObserver>
        <p class="self-end mx-1 mb-1 mt-auto text-white drop-shadow-lg">Continue -></p>    
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
    fields: [
      { name: "First Name", type: "text", isPassword: false, index: count++, id:"firstname", rules:"required",value:"" },
      { name: "Last Name", type: "text", isPassword: false, index: count++, id:"lastname", rules:"required",value:"" },
      { name: "Email", type: "text", isPassword: false, index: count++, id:"email", rules:"required|email",value:"" },
      { name: "Password", type: "text", isPassword: true, index: count++, id:"password", rules:"required|min:6",value:"" },
      { name: "Password Confirmation", type: "text", isPassword: true, index: count++, id:"confirm", rules:"required|password:@password",value:"" },
      { name: "Grade", type: "text", isPassword: false, index: count++, id:"grade", rules:"required",value:"" }, 
    ]
  }),
};
</script>
