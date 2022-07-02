<template>
  <body class="flex flex-col min-h-screen">
    <AuthHeader />

    <main class="flex flex-grow justify-center">
      <!-- Add sign up form here? -->
      <div class="w-11/12 max-w-lg flex flex-col items-center bg-green drop-shadow-lg">
        <form class="flex flex-col w-11/12 mx-6 my-8">
          <InputField v-for="field in fields" :key="field.index" :fieldName="field.name" :fieldType="field.type"/>
        </form>
        <p class="self-end mx-1 mb-1 mt-auto text-white drop-shadow-lg">Continue -></p>
      </div>
    </div>
    <AuthFooter />
  </body>
</template>

<script>
let count = 0;
export default {
  name: 'signup-page',
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
