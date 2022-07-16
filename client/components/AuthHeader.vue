<template>
  <div>
    <div class="flex justify-center mt-10 mb-6">
      <img class="w-16" src="~/static/logo.svg" alt="Elucidate Logo" />
    </div>
    <div v-if="pageTitle !== ''" class="flex justify-center items-center my-5">
      <img class="w-8 mx-2" src="~/static/personIcon.svg" alt="User Icon" />
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
