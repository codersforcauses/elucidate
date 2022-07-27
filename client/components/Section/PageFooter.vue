<template>
  <footer class="h-20">
    <div class="flex items-center justify-around mb-2 text-sm font-bold">
      <div class="flex justify-center w-full">
        <NuxtLink to="/" class="mx-4">Home</NuxtLink>
        <NuxtLink to="/quiz" class="mx-4">Quiz</NuxtLink>
        <NuxtLink to="/about" class="mx-4">About</NuxtLink>
      </div>
      <div class="flex justify-center w-full">
        <nuxt-img
          src="branding/logo_full.png"
          class="h-12"
          alt="Elucidate Logo"
        />
      </div>
      <div class="flex justify-center w-full">
        <NuxtLink to="/about" class="mx-4">Resources</NuxtLink>
        <NuxtLink to="/" class="mx-4">Contact</NuxtLink>
        <NuxtLink to="/quiz" class="mx-4">Sponsors</NuxtLink>
      </div>
    </div>
    <hr />
    <div class="flex items-center justify-center py-8 text-4xl text-gray-400">
      <a href="https://www.facebook.com/AtarSurvivalGuide/">
        <font-awesome-icon :icon="['fab', 'fa-facebook']" class="mx-4" />
      </a>
      <a href="https://www.instagram.com/atar_survival_guide/">
        <font-awesome-icon :icon="['fab', 'fa-instagram']" class="mx-4" />
      </a>
      <a href="https://www.youtube.com/channel/UC3d8MUFzDD01IoeJCDazSpg">
        <font-awesome-icon :icon="['fab', 'fa-youtube']" class="mx-4" />
      </a>
      <a href="https://www.linkedin.com/company/atar-survival-guide/">
        <font-awesome-icon :icon="['fab', 'fa-linkedin']" class="mx-4" />
      </a>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'PageFooter',
};
</script>
