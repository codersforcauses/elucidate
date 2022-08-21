<template>
  <div class="inline-block relative w-full">
    <div class="justify-self-start text-sm m-5">
      {{ quizdata.question_desc[curr - 1] }}
    </div>
    <!-- Question Choices -->
    <div v-if="quizdata.question_type[0] === 'mcq'">
      <div class="justify-center grid grid-cols-1 w-full select-none">
        <div
          v-for="(choice, index) in quizdata.question_choices[
            curr - 1
          ]"
          :key="index"
          class="py-2 px-4 my-5 mx-20 z-50 text-center shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm"
        >
          {{ choice }}
        </div>
      </div>
    </div>

    <!-- Short Answer Choices -->
    <div v-if="quizdata.question_type[0] === 'short_answer'">
      <div class="p-5">
        <div class="bg-teal-200 min-h-full p-5 rounded-sm shadow-md">
          <div>Your Answer</div>
          <div
            class="m-2 bg-white border border-b-black rounded-md w-full"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import dummyjson from './dummy.json';
export default {
  name: 'ReviewCard',
  props: ['quizdata', 'max', 'not_found'],
  data: function () {
    return {
      curr: 1,
      answer: '',
      answerArray: [],
      completed: false,
    };
  },
};
</script>
