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
    <nuxt-img src="shapes.svg" class="w-72 mt-4" alt="Shapes" />
  </div>
</template>

<script>
export default {
  computed: {
    title() {
      const rawTitle = this.$route.name;
      // Make first letter uppercase
      return (
        (rawTitle.charAt(0).toUpperCase() + rawTitle.slice(1))
          // Change dashes to spaces
          .replace(/-/, ' ')
      );
    },
  },
};
</script>

<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
