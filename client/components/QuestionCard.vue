<template>
  <div
    class="relative max-w-full pb-4 bg-violet-300 rounded-sm shadow-md min-h-full"
  >
    <!-- Question Number -->
    <div class="flex bg-teal-100 py-4 rounded-sm">
      <div v-if="!this.not_found" class="w-1/3 px-5">
        <h1>Question {{ this.curr }} / {{ this.max }}</h1>
      </div>
      <ProgressBar v-if="!this.not_found" :curr="this.curr" :max="this.max" />
    </div>

    <!-- Non-Header Question Block -->
    <div v-if="!this.not_found">
      <!-- Question Detail -->
      <div class="">
        <div class="justify-self-start text-sm m-5">
          {{ this.quizdata.question_desc[this.curr - 1] }}
        </div>
      </div>

      <!-- Question Choices -->
<<<<<<< HEAD
      <div
        class="justify-center grid grid-cols-1 grid-rows-4 my-8 mx-20 select-none flex"
      >
        <button
          class="py-2 px-4 my-5 mx-5 z-50 shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm border-black btn-primary hover:text-white hover:bg-black focus:outline-none active:shadow-none"
          v-for="(choice, index) in this.quizdata.question_choices[
            this.curr - 1
          ]"
        >
          {{ choice }}
=======
      <div class="justify-center grid grid-cols-1 grid-rows-4 my-8 select-none flex">
        <!-- <input type="radio" id="html" name="fav_language" value="HTML" class="py-2 px-4 my-5 mx-5 z-50 shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm border-black btn-primary hover:text-white hover:bg-black focus:outline-none active:shadow-none">
        <label for="html">HTML</label><br>
        <input type="radio" id="css" name="fav_language" value="CSS">
        <label for="css">CSS</label><br>
        <input type="radio" id="javascript" name="fav_language" value="JavaScript">
        <label for="javascript">JavaScript</label> -->
        
        <button class="py-2 px-4 my-5 mx-5 z-50 shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm border-black btn-primary hover:text-white hover:text-gray-700 hover:bg-gray-200 focus:outline-none active:shadow-none" v-for="(choice, index) in this.quizdata.question_choices[this.curr-1]">
          <input type="radio" :id="index" name="answer_form" :value="choice" v-model="answer">
          <label :for="index">{{choice}}
          <svg aria-hidden="true" class="ml-3 w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
          </label><br>
>>>>>>> a9aab3ffed850116dc13e1e9d4f6f3ae629219d0
        </button>
      </div>

      <!-- Submit button -->
      <input type="submit" value="Submit Answer"
        data-mdb-ripple="true"
        data-mdb-ripple-color="light"
        class="inline-block float-right text-center px-6 py-1 my-5 mx-24 bg-indigo-500 text-white text-md rounded-lg shadow-md hover:bg-indigo-600 hover:shadow-lg focus:bg-indigo-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-700 active:shadow-lg transition duration-300 ease-in-out"
      >

      <!-- Next/Back buttons 
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
      </div> -->
    </div>
    <div v-else class="content-center">
      <h1 class="text-center text-4xl text-white mt-20">
        Ooops! Quiz Not Found
      </h1>
    </div>
  </div>
</template>

<script>
import ProgressBar from './ProgressBar.vue';
import dummyjson from './dummy.json';
export default {
<<<<<<< HEAD
  name: 'QuestionCard',
  data: function () {
    return {
      curr: 1,
    };
  },
  methods: {
    nextQuestion() {
      if (this.curr == this.max) return; // TODO: Fade out styling for Next button (this.currr == this.max)
      this.curr++;
=======
    name: "QuestionCard",
    data: function () {
        return {
            curr: 1,
            answer: null
        };
    },
    methods: {
      nextQuestion(){
        if(this.curr == this.max) return // TODO: Fade out styling for Next button (this.currr == this.max)
        this.curr++
        console.log(this.answer)
      },
      prevQuestion(){
        if(this.curr == 1) return // TODO: Fade out Styling for Prev button (this.curr == 1)
        this.curr--
      }
>>>>>>> a9aab3ffed850116dc13e1e9d4f6f3ae629219d0
    },
    prevQuestion() {
      if (this.curr == 1) return; // TODO: Fade out Styling for Prev button (this.curr == 1)
      this.curr--;
    },
  },
  created() {
    if (this.quizdata === null) {
      this.not_found = true;
    }
  },
  components: { ProgressBar },
  props: ['quizdata', 'max', 'not_found'],
};
</script>
