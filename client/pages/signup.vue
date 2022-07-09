<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader :pageTitle="title" />

    <div class="flex flex-grow justify-center">
      <!-- Add sign up form here? -->
      <TealBox>
        <form class="flex flex-col w-11/12 mx-6 my-8">
          <InputField v-for="field in fields" 
          :key="field.index" 
          :fieldName="field.name" 
          :fieldType="field.type" 
          :isPassword="field.isPassword" />
        </form>
        <button type="button" class="self-end mx-6 mb-3 mt-auto text-white">Continue</button>
      </TealBox>
    </div>
    <AuthFooter />
  </div>
</template>

<script>
let count = 0;
export default {
  name: 'signup-page',
  data: () => ({
    title: "Sign-Up",
    fields: [
      { name: "First Name", type: "text", isPassword: false, index: count++ },
      { name: "Last Name", type: "text", isPassword: false, index: count++ },
      { name: "Email", type: "text", isPassword: false, index: count++ },
      { name: "Password", type: "text", isPassword: true, index: count++ },
      { name: "Confirm Password", type: "text", isPassword: true, index: count++ },
      { name: "Grade", type: "text", isPassword: false, index: count++ },
    ]
  })
};
</script>
