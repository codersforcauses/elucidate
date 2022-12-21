<template>
  <div class="flex mx-20">
    <div>
      <QuizDetailCard
        v-if="!not_found"
        :topic-name="quiz_name"
        :total-ques="quiz_num_questions"
      />
    </div>
    <div
      class="relative w-full pb-4 ml-4 bg-indigo-300 rounded-sm shadow-md min-h-full"
    >
      <div class="flex bg-teal-100 p-4 rounded-sm">Quiz Review</div>
      <div class="flex">
        <div class="text-sm bg-teal-200 w-24 h-24 rounded-lg m-5 p-2">
          <div>Question {{ quiz_num_questions }}</div>
          <div>Mark</div>
        </div>
        <reviewCard
          :not_found="not_found"
          :quizdata="quizdata"
          :max="quiz_num_questions"
        />
      </div>
      <!-- Explanation -->
      <div
        v-if="quizdata.answer[0]"
        class="inline-block bg-teal-200 rounded-lg p-4 ml-36"
      >
        <div>Your answer is correct</div>
      </div>
    </div>
  </div>
</template>

<script>
import dummyjson from '../components/Solve/dummy.json';
export default {
  name: 'QuizReview',
  data() {
    return {
      quizID: parseInt(this.$route.query.quizid),
      quizdata: null,
      quiz_name: null,
      quiz_num_questions: null,
      not_found: false,
    };
  },
  created() {
    // TODO: Use API to process route.query.quizID

    // process dummyjson
    for (const quiz of dummyjson) {
      if (this.quizID === quiz.quiz_id) {
        this.quizdata = quiz;
        // Fill data properties
        this.quiz_name = this.quizdata.quiz_name;
        this.quiz_num_questions = 1;
        break;
      }
    }
  },
};
</script>
