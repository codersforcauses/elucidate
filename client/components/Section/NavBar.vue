<template>
  <nav class="z-50 flex items-center justify-between h-20 bg-white shadow-xl">
    <div class="flex items-center text-gray-600">
      <NuxtLink to="/" class="h-12 ml-4 lg:ml-32 -mt-2">
        <nuxt-img
          src="branding/logo_full.png"
          class="h-12 max-w-none"
          alt="Elucidate Logo Full"
        />
      </NuxtLink>
      <NuxtLink to="/" class="mx-4">Home</NuxtLink>
      <NuxtLink to="/quiz" class="mx-4">Quiz</NuxtLink>
      <NuxtLink to="/about" class="mx-4">About</NuxtLink>
    </div>
    <div class="flex items-center">
      <SearchBar class="hidden mr-24 xl:flex" />

      <div v-if="!this.$auth.loggedIn" class="whitespace-nowrap hidden sm:flex">
        <ButtonElement to="/login" type="primary" class="mr-10 md:mr-3">
          Log in
        </ButtonElement>
        <ButtonElement
          to="/sign-up"
          type="secondary"
          class="mr-10 hidden md:inline"
        >
          Sign up
        </ButtonElement>
      </div>

      <div v-else class="flex items-center">
        <NuxtLink to="/user-dashboard" class="mr-10 hidden xs:inline">
          <font-awesome-layers class="fa-2x">
            <font-awesome-icon :icon="['fas', 'circle']" class="text-green" />
            <font-awesome-icon
              :icon="['fas', 'user']"
              class="text-lg text-white"
            />
          </font-awesome-layers>
        </NuxtLink>
      </div>
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
