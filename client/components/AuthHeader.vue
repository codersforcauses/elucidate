<template>
  <div>
    <div class="flex justify-center my-5">
      <img class="w-11" src="~/assets/logo.png" />
    </div>
    <div  v-if="pageTitle !== ''" class="flex justify-center items-center my-5 ">
      <img class="w-8 mx-2" src="~/assets/personIcon.svg" />
      <p class="text-2xl italic">{{pageTitle}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthHeader',
  props: {
    pageTitle: String,
  }
};
</script>
