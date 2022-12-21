<template>
  <div
    class="relative w-full pb-4 bg-indigo-300 rounded-sm shadow-md min-h-full"
  >
    <!-- Question Number -->
    <div class="flex bg-teal-100 py-4 rounded-sm">
      <div v-if="!not_found" class="w-1/3 px-5">
        <h1>Question {{ curr }} / {{ max }}</h1>
      </div>
      <!-- <ProgressBar v-if="!not_found" :curr="curr" :max="max" /> -->
    </div>

    <!-- Non-Header Question Block -->
    <div v-if="!not_found">
      <!-- Question Detail -->
      <div class="">
        <div class="justify-self-start text-sm m-5">
          {{ quizdata.question_desc[curr - 1] }}
        </div>
      </div>

      <!-- Question Choices -->
      <div v-if="quizdata.question_type[0] === 'mcq'">
        <div class="justify-center grid grid-cols-1 w-full select-none">
          <select
            v-model="answer"
            multiple
            class="overflow-hidden border-transparent focus:outline-none bg-transparent h-64"
          >
            <option
              v-for="(choice, index) in quizdata.question_choices[curr - 1]"
              :key="index"
              class="py-2 px-4 my-5 mx-20 z-50 text-center shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm border-black btn-primary hover:text-gray-700 hover:bg-gray-200 focus:outline-none active:shadow-none"
            >
              {{ choice }}
            </option>
          </select>
          <div>Selected: {{ answer }}</div>
          <div>Answer array: {{ answerArray }}</div>
        </div>
      </div>

      <!-- Short Answer Choices -->
      <div v-if="quizdata.question_type[0] === 'short_answer'">
        <div class="p-5">
          <div class="bg-teal-200 min-h-full p-5 rounded-sm shadow-md">
            <div>Answer</div>
            <textarea
              id="message"
              rows="4"
              class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Your message..."
            ></textarea>
          </div>
        </div>
      </div>

      <!-- Numerical Answer Choices -->
      <div v-if="quizdata.question_type[0] === 'numerical'"></div>
    </div>
    <div v-else class="content-center">
      <h1 class="text-center text-4xl text-white mt-20">
        Ooops! Quiz Not Found
      </h1>
    </div>
    <!-- Submit button -->
    <input
      v-if="!completed"
      type="submit"
      value="Submit Answer"
      data-mdb-ripple="true"
      data-mdb-ripple-color="light"
      class="inline-block float-right text-center px-6 py-1 my-5 mx-24 bg-indigo-500 text-white text-md rounded-lg shadow-md hover:bg-indigo-600 hover:shadow-lg hover:cursor-pointer focus:bg-indigo-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-700 active:shadow-lg transition duration-300 ease-in-out"
      @click="submitAnswer"
    />

    <!-- Main modal -->
    <div
      v-show="completed"
      tabindex="-1"
      class="bg-gray-800/80 overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-full justify-center items-center flex"
      aria-modal="true"
      role="dialog"
    >
      <div class="relative p-4 w-full max-w-2xl h-full md:h-auto">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div
            class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600"
          >
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
              Well done, you have completed the quiz!
            </h3>
          </div>
          <!-- Modal body -->
          <div class="p-6 space-y-6">
            <p
              class="text-base leading-relaxed text-gray-500 dark:text-gray-400"
            >
              You just finished the {{ quizdata.quiz_name }} quiz with a total
              of {{ curr }} questions.
            </p>
          </div>
          <!-- Modal footer -->
          <div
            class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
          >
            <NuxtLink
              to="/"
              class="text-white bg-red hover:bg-red-400 focus:ring-4 focus:outline-none rounded-lg text-sm font-medium px-5 py-2.5 focus:z-10"
              >Review</NuxtLink
            >
            <NuxtLink
              to="/"
              class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10"
              >Home</NuxtLink
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuestionCard',
  props: ['quizdata', 'max', 'not_found'],
  data: function () {
    return {
      curr: 1,
      answer: '',
      answerArray: [],
      completed: false,
    };
  },
  methods: {
    // nextQuestion() {
    //   if (this.curr == this.max) return; // TODO: Fade out styling for Next button (this.currr == this.max)
    //   this.curr++;
    // },
    prevQuestion() {
      if (this.curr == 1) return; // TODO: Fade out Styling for Prev button (this.curr == 1)
      this.curr--;
    },
    submitAnswer() {
      if (this.curr < this.max) {
        this.curr++;
      } else {
        this.completed = true;
      }
      this.answerArray.push(this.answer);
    },
    created() {
      if (this.quizdata === null) {
        this.not_found = true;
      }
    },
  },
};
</script>
