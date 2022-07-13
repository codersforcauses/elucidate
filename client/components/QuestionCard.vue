<template>
  <div class="relative w-128 pb-4 bg-violet-300 rounded-sm shadow-md">
    <!-- Question Number -->
    <div class="flex bg-teal-100 py-4 rounded-sm">
      <div class="w-1/3 px-5">
        <h1>Question {{this.curr}} / {{this.max}}</h1>
      </div> 
        <ProgressBar 
        :curr = "this.curr"
        :max = "this.max"
        />
    </div>
    <!-- Question Detail -->
    <div class="">
        <div class="justify-self-start text-sm m-5 ">
            {{this.quizdata.question_desc[this.curr-1]}}
        </div> 
    </div>

    <!-- Question Choices -->
    <div class = "justify-center grid grid-cols-1 grid-rows-4 my-8 select-none flex">
      <button class="py-2 px-4 my-5 mx-5 z-50 shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm border-black btn-primary hover:text-white hover:bg-black focus:outline-none active:shadow-none" v-for="(choice, index) in this.quizdata.question_choices[this.curr-1]"> {{choice}}</button>
    </div>

    <!-- Next/Back buttons -->
    <div class="flex justify-end px-5 mt-2">
      <button>
        <div class="inline-block text-center text-xs text-white py-0.5 px-2 mr-1 bg-yellow-600 rounded-xl shadow-md hover:bg-yellow-700 hover:shadow-lg focus:bg-yellow-700 focus:shadow-lg focus:outline-none active:bg-yellow-800 active:shadow-lg transition duration-300 ease-in-out" @click="prevQuestion">
            Back
        </div>
      </button>
      <button>
        <div class="inline-block text-center text-xs text-white py-0.5 px-2 bg-pink-600 rounded-xl shadow-md hover:bg-pink-700 hover:shadow-lg focus:bg-pink-700 focus:shadow-lg focus:outline-none active:bg-pink-800 active:shadow-lg transition duration-300 ease-in-out" @click="nextQuestion">
            Next
        </div>
      </button>
    </div>

  </div>
</template>

<script>
import ProgressBar from './ProgressBar.vue'
import dummyjson from './dummy.json'
export default {
    name: "QuestionCard",
    data: function () {
        return {
            quizID: parseInt(this.$route.query.quizid),
            curr: 1,
            max: null,
            quizdata: null,
        };
    },
    methods: {
      nextQuestion(){
        if(this.curr == this.max) return // TODO: Fade out styling for Next button (this.currr == this.max)
        this.curr++
      },
      prevQuestion(){
        if(this.curr == 1) return // TODO: Fade out Styling for Prev button (this.curr == 1)
        this.curr--
      }
    },
    components: { ProgressBar },
    created() {
      // TODO: Use API to process route.query.quizID
      //process dummyjson
      for (const quiz of dummyjson) {
        // console.log(quiz, quiz.quiz_id)
        if (this.quizID === quiz.quiz_id) {
          this.quizdata = quiz
          // console.log(this.quizdata)
          this.max = this.quizdata.question_choices[0].length
          break
        }
      }
      if (this.max === null){
        this.quizdata = dummyjson[0]
        this.max = this.quizdata.question_choices.length
      }
    },
};
</script>