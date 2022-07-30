<template>
  <div
    class="flex flex-col items-center content-center min-w-full min-h-screen"
  >
    <AuthHeader :page-title="$route.name" />
    <Nuxt />
    <AuthFooter />
  </div>
</template>
<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
