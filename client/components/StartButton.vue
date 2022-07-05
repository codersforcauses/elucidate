<template>
  <div class="flex justify-center">
    <a v-bind:href="quizPage"
    data-mdb-ripple="true" data-mdb-ripple-color="light"
    class="inline-block text-center px-6 py-1 mt-10 mb-3 w-2/5
    bg-teal-300 text-white text-lg rounded-3xl shadow-md 
    hover:bg-teal-400 hover:shadow-lg 
    focus:bg-teal-400 focus:shadow-lg focus:outline-none focus:ring-0 
    active:bg-teal-500 active:shadow-lg transition duration-300 ease-in-out">Start</a>
  </div>
</template>

<script>
export default {
  name:'StartButton',
  data:function(){
    return{
      quizPage:'http://localhost:8080/quiz-page'
    };
  }
};
</script>