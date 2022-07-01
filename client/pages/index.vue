<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader />
    <div class="flex justify-center">
      Sign Up
    </div>
    <div class="flex flex-grow justify-center">
      <!-- Add sign up form here? -->
      <div class="w-11/12 max-w-lg flex flex-col items-center bg-teal-300 drop-shadow-lg">
        <form class="flex flex-col w-11/12 mx-10 my-12">
          <label>First Name</label>
          <input type="text" class="w-full"><br>
          <label>Last Name</label>
          <input type="text" class="w-full"><br>
          <label>Email</label>
          <input type="email" class="w-full"><br>
          <label>Password</label>
          <input type="text" class="w-full"><br>
          <label>Confirm Password</label>
          <input type="text" class="w-full"><br>
          <label>Grade</label>
          <input type="text" class="w-full"><br>
        </form>
        <p class="self-end mx-1 mb-1 mt-auto text-white drop-shadow-lg">Continue -></p>
      </div>
    </div>

    <AuthFooter />
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
};
</script>
