<template>
  <div>
    <div class="container mx-auto pl-20">
      <!-- Section 1 -->
      <div class="grid lg:grid-cols-2 gap-x-14 mt-36 mb-52 items-center">
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
    <!-- Section 2 (sneak-peak of the quizzes) -->
    <div class="bg-indigo-500 pt-20 pb-40">
      <h2 class="text-white text-5xl text-center py-20">Look at our quizzes</h2>
      <div class="grid lg:grid-cols-3 gap-14 mx-36 content-evenly">
        <div><QuizCard /></div>
        <div><QuizCard /></div>
        <div><QuizCard /></div>
      </div>
    </div>
  </div>
</template>

<script>
import haveAccBtn from '~/components/haveAccBtn.vue';
import SearchBar from '~/components/searchBar.vue';
import AuthFooter from '~/components/AuthFooter.vue';
import QuizCard from '~/components/QuizCard.vue';
export default {
  components: { 
    haveAccBtn,
    SearchBar,
    AuthFooter, 
    QuizCard,
  },
  name: 'IndexPage',
  data:function() {
    return {
      illustration: require("~/assets/QAimage.svg"),
    };
  }
};
</script>
