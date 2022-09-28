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
      const rawPath = this.$route.path;

      // Remove trailing '/'
      let title =
        rawPath.charAt(rawPath.length - 1) === '/'
          ? rawPath.substring(0, rawPath.length - 1)
          : rawPath;
      // Remove directories
      title = title.split('/').pop();
      // Make first letter uppercase
      title = title.charAt(0).toUpperCase() + title.slice(1);
      // Change dashes to spaces
      title = title.replace(/-/, ' ');
      return title;
    },
  },
};
</script>

<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
