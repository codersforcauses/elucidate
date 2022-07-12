<template>
  <div class="relative w-128 pb-4 bg-violet-300 rounded-sm shadow-md">
    <!-- Question Number -->
    <div class="flex bg-teal-100 py-4 rounded-sm">
      <div class="w-1/4 px-5">
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
            {{this.dummy[0].question_desc[this.curr-1]}}
        </div> 
    </div>

    <!-- Question Choices -->
    <div>
      <li v-for="(choice, index) in this.dummy[0].question_choices[this.curr-1]"> {{choice}}</li>
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
            quizID: "num",
            curr: 1,
            max: dummyjson[0].question_desc.length,
            dummy: dummyjson
        };
    },
    methods: {
      nextQuestion(){
        if(this.curr == this.max) return // TODO: Fade out styling for Next button (this.currr == this.max)
        this.curr++
        console.log(this.curr);
        console.log(this.dummy)
      },
      prevQuestion(){
        if(this.curr == 1) return // TODO: Fade out Styling for Prev button (this.curr == 1)
        this.curr--
        console.log(this.curr);
      }
    },
    components: { ProgressBar }
};
</script>