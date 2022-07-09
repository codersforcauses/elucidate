<template>
  <div>
    <div class="flex justify-center mt-10 mb-6">
      <img class="w-16" src="~/assets/logo.svg" alt="Elucidate Logo" />
    </div>
    <h1
      v-if="pageTitle !== ''"
      class="italic text-3xl my-4 mr-7 flex gap-x-3 whitespace-nowrap"
    >
      <img class="w-8" src="~/assets/avatar.svg" alt="Sign In Logo" />
      Sign In
    </h1>
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
