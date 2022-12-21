<template>
  <div class="flex m-20">
    <div>
      <QuizDetailCard
        v-if="!not_found"
        :topic-name="topics"
        :total-ques="quiz_num_questions"
      />
    </div>
    <!-- <div class="ml-10 min-w-[50%] min-h-[40%]">
      <QuestionCard
        :not_found="not_found"
        :quizdata="quizdata"
        :max="quiz_num_questions"
      />
    </div> -->
  </div>
  <!-- <ProgressBar></ProgressBar> -->
</template>

<script>
import dummyjson from '../components/Solve/dummy.json';
export default {
  name: 'QuizSolve',
  data() {
    return {
      quizID: parseInt(this.$route.query.quizid),
      quizdata: null,
      quiz_name: null,
      quiz_num_questions: null,
      not_found: false,
    };
  },
  async mounted() {
    const res = await this.$axios.$get(`quizzes/${this.$route.query.quizid}`);
    console.log(res);

    // if (this.quizdata === null) {
    //   this.not_found = true;
    // }
  },
};
</script>
