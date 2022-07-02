<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader />
    <div class="flex justify-center">
      Sign Up
    </div>
    <div class="flex flex-grow justify-center">
      <!-- Add sign up form here? -->
      <div class="w-11/12 max-w-lg flex flex-col items-center bg-teal-200 drop-shadow-lg">
        <form class="flex flex-col w-11/12 mx-6 my-8">
          <div v-for="field in fields" :key="field.index">
            <label>{{field.name}}</label>
            <input type="field.name" class="w-full h-10 drop-shadow-lg mt-2 mb-4">
          </div>
        </form>
        <p class="self-end mx-1 mb-1 mt-auto text-white drop-shadow-lg">Continue -></p>
      </div>
    </div>
    <AuthFooter />
  </div>
</template>

<script>
let count = 0;
export default {
  name: 'IndexPage',
  data: () => ({
    fields: [
      { name: "First Name", type: "text", index: count++ },
      { name: "Last Name", type: "text", index: count++ },
      { name: "Email", type: "text", index: count++ },
      { name: "Password", type: "text", index: count++ },
      { name: "Confirm Password", type: "text", index: count++ },
      { name: "Grade", type: "text", index: count++ },
    ]
  })
};
</script>
