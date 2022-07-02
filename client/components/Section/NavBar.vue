<template>
  <nav class="h-20 flex items-center shadow-xl justify-between">
    <div class="flex">
      <NuxtLink to="/" class="mx-4 font-Montserrat">Home</NuxtLink>
      <NuxtLink to="/quiz" class="mx-4 font-Montserrat">Quiz</NuxtLink>
      <NuxtLink to="/about" class="mx-4 font-Montserrat">About</NuxtLink>
    </div>
    <div class="flex items-center">
      <InputSearchBar class="mr-24" />
      <!-- TODO: Do we want the button to open a pop up window or redirect to a
      login page? -->
      <InputButtonElement type="primary" class="mr-3"
        >Log in</InputButtonElement
      >
      <InputButtonElement type="secondary" class="mr-10"
        >Sign up</InputButtonElement
      >
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>
<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
