<template>
  <div class="h-full w-full">
    <div class="grid grid-rows-auto mr-10 flex space-y-2">
      <!-- 9 cols, two per property, one for score -->
      <div class="py-1 px-6 grid grid-cols-7 text-lightgrey font-bold flex">
        <h1 class="col-span-2">Title</h1>
        <h1 class="col-span-2">Tags</h1>
        <h1 class="col-span-2">Date Created</h1>
        <h1>Your Score</h1>
      </div>
      <QuizListItem
        @showQuiz="(selectedQuiz) => showSelectedQuiz(selectedQuiz)"
        v-for="(quiz, index) in quizzes"
        :key="index"
        :Quiz="quiz"
      />
    </div>
    <QuizCard v-if="showQuizModal" :quiz="quizToShow" @closeQuiz="closeQuizModal()"/>
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
    showQuizModal: false,
    quizToShow: {},
  }),
  methods: {
    showSelectedQuiz: function (selectedQuiz) {
      this.quizToShow = selectedQuiz;
      this.showQuizModal = true;
    },
    closeQuizModal: function () {
      this.showQuizModal = false;
    },
  }
};
</script>
