<template>
  <div
    class="flex flex-col items-center content-center min-w-full min-h-screen"
  >
    <AuthHeader :page-title="title" />
    <Nuxt />
    <AuthFooter />
  </div>
</template>

<script>
export default {
  computed: {
    title() {
      // Make first letter uppercase
      const rawTitle = this.$route.name;
      return rawTitle.charAt(0).toUpperCase() + rawTitle.slice(1);
    },
  },
};
</script>

<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
