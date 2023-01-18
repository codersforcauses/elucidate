<template>
  <div class="flex m-20">
    <div>
      <QuizDetailCard
        v-if="!notFound"
        :subject-name="subjectName"
        :topics="topics"
        :total-ques="numQuestions"
        :quizID="quizID"
        :curr="currQuestion"
      />
    </div>
    <keep-alive>
      <div class="ml-10 min-w-[50%] min-h-[40%]">
        <QuestionCard
          :quizID="quizID"
          :notFound="notFound"
          :questionData="questionData"
          :max="numQuestions"
          :curr="currQuestion"
        />
      </div>
    </keep-alive>
  </div>
  <!-- <ProgressBar></ProgressBar> -->
</template>

<script>
export default {
  name: 'QuizSolve',
  data() {
    return {
      quizID: parseInt(this.$route.query.quizid),
      currQuestion: parseInt(this.$route.query.question) || 1,
      questionData: null,
      numQuestions: null,
      subjectName: null,
      notFound: false,
      topics: null,
    };
  },
  watch: {
    '$route.query': '$fetch',
  },
  async fetch() {
    this.currQuestion = parseInt(this.$route.query.question) || 1;
    const res_quiz = await this.$axios.$get(
      `quizzes/${this.$route.query.quizid}`
    );

    const res_attempt = await this.$axios.$get(
      `take-quiz/save/${this.$route.query.quizid}`
    );

    this.subjectName = res_quiz.questions[0].subject.name;
    this.numQuestions = res_quiz.questions.length;
    this.topics = res_quiz.topics;
    if (this.currQuestion < 1 || this.currQuestion > this.numQuestions) {
      this.notFound = true;
    }
    this.questionData = res_quiz.questions[this.currQuestion - 1];
  },
};
</script>
