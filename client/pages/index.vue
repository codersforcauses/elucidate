<template>
  <div class="container mx-auto pl-20">
    <div class="grid grid-cols-2 gap-x-10 items-center">
      <div>
        <h1 class="text-black-400 text-6xl leading-snug mb-10">What do you want <br>to learn today?</h1>
        <SearchBar />
        <haveAccBtn />
        <AuthFooter />
      </div>
      <div>
        <img v-bind:src="illustration">
      </div>
    </div>
  </div>
</template>

<script>
import haveAccBtn from '~/components/haveAccBtn.vue';
import SearchBar from '~/components/searchBar.vue';
import AuthFooter from '~/components/AuthFooter.vue';
export default {
  components: { 
    haveAccBtn,
    SearchBar,
    AuthFooter, 
  },
  name: 'IndexPage',
  data:function() {
    return {
      illustration: require("~/assets/QAimage.svg"),
    };
  }
};
</script>
