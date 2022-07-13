<template>
  <div class="flex m-20">
    <div>
      <QuizDetailCard 
        v-if="!this.not_found"
        :topicName="this.quiz_name"
        :totalQues = "this.quiz_num_questions"
      />
    </div>
    <div class="ml-10 min-w-[50%] min-h-[40%]">
      <QuestionCard 
        :not_found = "this.not_found"
        :quizdata = "this.quizdata"
        :max = "this.quiz_num_questions"
      />
    </div>
  </div>
  <!-- <ProgressBar></ProgressBar> -->
</template>

<script>
import dummyjson from '../components/dummy.json'
export default {
  name: 'quizSolve',
  data() {
    return {
      quizID: parseInt(this.$route.query.quizid),
      quizdata: null,
      quiz_name: null,
      quiz_num_questions: null,
      not_found: false
    }
  },
  created() {
    // TODO: Use API to process route.query.quizID

    //process dummyjson
    for (const quiz of dummyjson) {
      if (this.quizID === quiz.quiz_id) {
        this.quizdata = quiz
        // Fill data properties
        this.quiz_name = this.quizdata.quiz_name
        this.quiz_num_questions = this.quizdata.question_choices.length
        break
      }
    }

    // TODO: Return quiz not found when quiz_id does not exist
    if (this.quizdata === null){
      // Defaults to 0th dummy record when no valid quizid route query
      // this.quizdata = dummyjson[0]
      this.not_found = true
    }


  
  },

};
</script>
