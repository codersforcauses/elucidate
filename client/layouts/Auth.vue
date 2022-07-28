<template>
  <div
    class="flex flex-col items-center content-center min-w-full min-h-screen p-5"
  >
    <nuxt-img src="branding/logo.svg" class="w-16" alt="Elucidate Logo" />
    <div class="flex items-center my-5 mr-10">
      <font-awesome-layers class="fa-2x mx-3">
        <font-awesome-icon :icon="['fas', 'circle']" class="text-green" />
        <font-awesome-icon :icon="['fas', 'user']" class="text-lg text-white" />
      </font-awesome-layers>
      <p class="text-3xl italic">{{ title }}</p>
    </div>
    <Nuxt />
    <nuxt-img src="shapes.svg" class="w-72 mt-auto" alt="Shapes" />
  </div>
</template>

<script>
export default {
  computed: {
    title() {
      // Seperate words in the pages name provided it is in PascalCase
      const rawTitle = this.$route.name;
      return rawTitle.replace(/[A-Z]/g, ' $&');
    },
  },
};
</script>

<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
