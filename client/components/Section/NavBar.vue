<template>
  <nav class="flex items-center justify-between h-20 bg-white shadow-xl">
    <div class="flex items-center text-gray-600">
      <NuxtLink to="/" class="h-12 ml-32 -mt-2">
        <nuxt-img
          src="branding/logo_full.png"
          class="h-12"
          alt="Elucidate Logo Full"
        />
      </NuxtLink>
      <NuxtLink to="/" class="mx-4">Home</NuxtLink>
      <NuxtLink to="/quiz" class="mx-4">Quiz</NuxtLink>
      <NuxtLink to="/about" class="mx-4">About</NuxtLink>
    </div>
    <div class="flex items-center">
      <SearchBar class="mr-24" />
      <ButtonElement to="/login-page" type="primary" class="mr-3"
        >Log in</ButtonElement
      >
      <ButtonElement to="/signup" type="secondary" class="mr-10"
        >Sign up</ButtonElement
      >
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style scoped lang="postcss">
.nuxt-link-exact-active {
  @apply font-bold;
}
</style>
