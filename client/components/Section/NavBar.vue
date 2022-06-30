<template>
  <nav class="h-[78px] flex items-center shadow-xl justify-between">
    <div>
      <NuxtLink to="/" class="mx-4 font-Montserrat">Home</NuxtLink>
      <NuxtLink to="/quiz" class="mx-4 font-Montserrat">Quiz</NuxtLink>
      <NuxtLink to="/about" class="mx-4 font-Montserrat">About</NuxtLink>
    </div>
    <div class="flex items-center">
      <div
        class="flex items-center h-10 bg-gray-200 rounded-md focus-within:outline focus-within:outline-2 focus-within:outline-gray-400"
      >
        <font-awesome-icon
          :icon="['fas', 'magnifying-glass']"
          class="mx-4 text-gray-400"
        />
        <input
          type="text"
          placeholder="Find a quiz"
          class="bg-transparent focus:outline-none"
        />
      </div>
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
