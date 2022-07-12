<template>
  <div>
    <div class="flex justify-center mt-10 mb-6">
      <nuxt-img src="branding/logo.svg" class="w-16" alt="Elucidate Logo" />
    </div>
    <div
      v-if="pageTitle !== ''"
      class="flex items-center justify-center my-5 mr-10"
    >
      <font-awesome-layers class="fa-2x mx-3">
        <font-awesome-icon :icon="['fas', 'circle']" class="text-green" />
        <font-awesome-icon :icon="['fas', 'user']" class="text-lg text-white" />
      </font-awesome-layers>
      <p class="text-2xl italic">{{ pageTitle }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthHeader',
  props: {
    pageTitle: String,
  },
};
</script>
