<template>
  <div class="flex flex-col items-center mt-5">
    <nuxt-img src="branding/logo.svg" class="w-16" alt="Elucidate Logo" />
    <div v-if="pageTitle !== ''" class="flex items-center my-5 mr-10">
      <font-awesome-layers class="fa-2x mx-3">
        <font-awesome-icon :icon="['fas', 'circle']" class="text-green" />
        <font-awesome-icon :icon="['fas', 'user']" class="text-lg text-white" />
      </font-awesome-layers>
      <p class="text-3xl italic">{{ pageTitle }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthHeader',
  props: {
    pageTitle: {
      type: String,
      default: '',
    },
  },
};
</script>
