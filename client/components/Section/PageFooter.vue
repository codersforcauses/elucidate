<template>
  <footer class="relative bottom-1 h-[78px]">
    <div class="flex items-center justify-around font-bold text-sm">
      <div class="w-full flex justify-center">
        <NuxtLink to="/" class="mx-4 font-Montserrat">Home</NuxtLink>
        <NuxtLink to="/quiz" class="mx-4 font-Montserrat">Quiz</NuxtLink>
        <NuxtLink to="/about" class="mx-4 font-Montserrat">About</NuxtLink>
      </div>
      <div class="w-full flex justify-center">
        <img src="~/assets/logo.png" class="h-14" />
      </div>
      <div class="w-full flex justify-center">
        <NuxtLink to="/about" class="mx-4 font-Montserrat">Resources</NuxtLink>
        <NuxtLink to="/" class="mx-4 font-Montserrat">Contact</NuxtLink>
        <NuxtLink to="/quiz" class="mx-4 font-Montserrat">Sponsors</NuxtLink>
      </div>
    </div>
    <hr />
    <div class="flex justify-center items-center py-8">
      <a href="https://www.facebook.com/AtarSurvivalGuide/">
        <img
          src="https://static.wixstatic.com/media/0fdef751204647a3bbd7eaa2827ed4f9.png/v1/fill/w_32,h_32,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/0fdef751204647a3bbd7eaa2827ed4f9.png"
          class="h-10 mx-2"
        />
      </a>
      <a href="https://www.instagram.com/atar_survival_guide/">
        <img
          src="https://static.wixstatic.com/media/01c3aff52f2a4dffa526d7a9843d46ea.png/v1/fill/w_32,h_32,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/01c3aff52f2a4dffa526d7a9843d46ea.png"
          class="h-10 mx-2"
        />
      </a>
      <a href="https://www.youtube.com/channel/UC3d8MUFzDD01IoeJCDazSpg">
        <img
          src="https://static.wixstatic.com/media/78aa2057f0cb42fbbaffcbc36280a64a.png/v1/fill/w_32,h_32,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/78aa2057f0cb42fbbaffcbc36280a64a.png"
          class="h-10 mx-2"
        />
      </a>
      <a href="https://www.linkedin.com/company/atar-survival-guide/">
        <img
          src="https://static.wixstatic.com/media/6ea5b4a88f0b4f91945b40499aa0af00.png/v1/fill/w_32,h_32,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/6ea5b4a88f0b4f91945b40499aa0af00.png"
          class="h-10 mx-2"
        />
      </a>
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
