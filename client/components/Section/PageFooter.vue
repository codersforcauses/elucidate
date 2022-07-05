<template>
  <footer class="relative bottom-1 h-[78px]">
    <div class="flex items-center justify-around font-bold text-sm">
      <div>
        <NuxtLink to="/" class="mx-4 font-Montserrat">Home</NuxtLink>
        <NuxtLink to="/quiz" class="mx-4 font-Montserrat">Quiz</NuxtLink>
        <NuxtLink to="/about" class="mx-4 font-Montserrat">About</NuxtLink>
      </div>
      <img src="~/assets/logo.png" class="h-14" />
      <div>
        <NuxtLink to="/about" class="mx-4 font-Montserrat">Resources</NuxtLink>
        <NuxtLink to="/" class="mx-4 font-Montserrat">Contact</NuxtLink>
        <NuxtLink to="/quiz" class="mx-4 font-Montserrat">Sponsors</NuxtLink>
      </div>
    </div>
    <hr />
    <div class="flex justify-center items-center py-8">
      <img src="~/assets/social_media_placeholder.png" class="h-10 mx-2" />
      <img src="~/assets/social_media_placeholder.png" class="h-10 mx-2" />
      <img src="~/assets/social_media_placeholder.png" class="h-10 mx-2" />
      <img src="~/assets/social_media_placeholder.png" class="h-10 mx-2" />
    </div>
  </footer>
</template>

<script>
export default {
  name: 'PageFooter',
};
</script>
<style scoped>
@import '@fontsource/montserrat';
@import '@fontsource/open-sans';
</style>
