<template>
  <nav class="h-[78px] flex items-center shadow-xl justify-between">
    <div>
      <NuxtLink to="/" class="font-Montserrat mx-4">Home</NuxtLink>
      <NuxtLink to="/quiz" class="font-Montserrat mx-4">Quiz</NuxtLink>
      <NuxtLink to="/about" class="font-Montserrat mx-4">About</NuxtLink>
    </div>
    <div>
      <input type="text" class="bg-gray-200 h-10 rounded-md" />
      <ButtonElement>Log in</ButtonElement>
      <ButtonElement>Sign up</ButtonElement>
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
