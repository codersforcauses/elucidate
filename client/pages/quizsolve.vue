<template>
  <div class="flex m-20">
    <div>
      <QuizDetailCard
        v-if="!notFound"
        :subject-name="subjectName"
        :topics="topics"
        :total-ques="numQuestions"
      />
    </div>
    <div class="ml-10 min-w-[50%] min-h-[40%]">
      <QuestionCard
        :notFound="notFound"
        :questionData="questionData"
        :max="numQuestions"
      />
    </div>
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
  async mounted() {
    const res = await this.$axios.$get(`quizzes/${this.$route.query.quizid}`);
    this.subjectName = res.questions[0].subject.name;
    this.numQuestions = res.questions.length;
    this.topics = res.topics;
    if (this.currQuestion < 1 || this.currQuestion > this.numQuestions) {
      this.notFound = true;
    }
    this.questionData = res.questions[this.currQuestion - 1];
    console.log(this.questionData);

    // if (this.questionData === null) {
    //   this.notFound = true;
    // }
  },
};
</script>
