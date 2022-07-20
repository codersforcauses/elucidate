<template>
  <div class="h-full w-full"> 
    <div class="grid grid-rows-auto mr-10">
      <div class="py-2 px-6 grid grid-cols-4 text-lightgrey/75 font-thin"> 
        <h1>Name</h1>
        <h1>Tags</h1>
        <h1>Author</h1>
        <h1>Date Created</h1>
      </div>
      <QuizListItem v-for="(quiz, index) in quizzes" :key="index" :Quiz="quiz"/>
      
    </div>
    
  </div> 
</template>

<script>
import QuizListItem from './QuizListItem.vue';
export default {
  components: { QuizListItem },
  name: 'QuizList',
  props: {
    quizzes: {
      type: Array,
      default: null,
    },
  },
  data: () => ({
    listItemStyles: 'h-10 my-4 p-10',
  }),
};
</script>
