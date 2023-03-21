<template>
  <div
    v-if="questionData"
    class="relative w-full pb-4 bg-indigo-300 rounded-sm shadow-md min-h-full"
  >
    <!-- Question Number -->
    <div
      class="flex flex-col lg:flex-row bg-teal-100 py-4 px-6 rounded-sm justify-between"
    >
      <div>
        <span class="mr-2">Question {{ curr }}:</span>
        <span class="font-bold mr-2">{{ questionData.question }}</span>
      </div>

      <div>{{ questionData.marks }} marks</div>
      <!-- <ProgressBar v-if="!notFound" :curr="curr" :max="max" /> -->
    </div>

    <!-- Non-Header Question Block -->
    <div v-if="!notFound" class="p-6">
      <!-- Question Choices -->
      <div v-if="questionData.question_type === 'MC'">
        <p class="mb-4">Answer</p>
        <div class="justify-center grid grid-cols-1 w-full select-none">
          <div v-for="(choice, index) in questionData.answer" :key="index">
            <input
              type="radio"
              v-model="answer"
              :value="choice.answer"
              :id="index"
              class="hidden"
            />
            <label
              :class="`py-2 px-4 mb-4 text-center shadow-md rounded-full bg-white  font-sans font-semibold text-sm border-black block btn-primary  hover:bg-gray-200 focus:outline-none active:shadow-none ${
                answer === choice.answer
                  ? '!bg-indigo-500 text-white'
                  : 'text-black'
              }`"
              :for="index"
              >{{ choice.answer }}</label
            >
          </div>
          <div>Selected: {{ answer }}</div>
        </div>
      </div>

      <!-- Short Answer Choices -->
      <div v-if="questionData.question_type === 'SA'">
        <p class="mb-4">Answer</p>
        <textarea
          v-model="answer"
          id="message"
          rows="4"
          class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
          placeholder="Your answer..."
        ></textarea>
      </div>

      <!-- Numerical Answer Choices -->
      <div v-if="questionData.question_type === 'NA'">
        <p class="mb-4">Answer</p>
        <input
          v-model="answer"
          type="text"
          placeholder="Your answer..."
          class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
        />
      </div>
    </div>
    <div v-else class="content-center">
      <span class="text-center text-4xl text-white mt-20">
        Ooops! Quiz Not Found
      </span>
    </div>
    <!-- Submit button -->
    <div v-if="curr !== 1">
      <input
        type="submit"
        value="Previous Question"
        class="text-center absolute bottom-4 left-4 p-2 bg-indigo-500 text-white text-md rounded-lg shadow-md hover:bg-indigo-600 hover:shadow-lg hover:cursor-pointer focus:bg-indigo-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-700 active:shadow-lg transition duration-300 ease-in-out"
        @click="prevQuestion"
      />
    </div>
    <div v-if="curr !== max">
      <input
        type="submit"
        value="Next Question"
        class="text-center absolute bottom-4 right-4 p-2 bg-indigo-500 text-white text-md rounded-lg shadow-md hover:bg-indigo-600 hover:shadow-lg hover:cursor-pointer focus:bg-indigo-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-700 active:shadow-lg transition duration-300 ease-in-out"
        @click="nextQuestion"
      />
    </div>
    <div v-else>
      <input
        v-if="!completed"
        type="submit"
        value="Submit Answer"
        data-mdb-ripple="true"
        data-mdb-ripple-color="light"
        class="text-center absolute bottom-4 right-4 p-2 bg-indigo-500 text-white text-md rounded-lg shadow-md hover:bg-indigo-600 hover:shadow-lg hover:cursor-pointer focus:bg-indigo-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-indigo-700 active:shadow-lg transition duration-300 ease-in-out"
        @click="submitAnswer"
      />
    </div>

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
              You just finished the quiz with a total of
              {{ curr }} questions.
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
  watch: {
    '$route.query': '$fetch',
  },
  name: 'QuestionCard',
  props: ['max', 'notFound', 'curr', 'quizID', 'questionData'],
  data: function () {
    return {
      answer: '',
      completed: false,
    };
  },
  async fetch() {
    await this.$axios
      .$get(`take-quiz/save/${this.quizID}/${this.curr}/`)
      .then((data) => {
        console.log(data);
        this.answer = data.selected_answer;
      })
      .catch((err) => {
        console.log(err);
        this.answer = '';
      });
  },
  methods: {
    async saveQuestion() {
      const question = parseInt(this.$route.query.question);
      const quizid = parseInt(this.$route.query.quizid);
      const res = await this.$axios
        .$post(`take-quiz/save/`, {
          selected_answer: this.answer,
          question: question,
          quiz: quizid,
        })
        .catch(
          await this.$axios.$patch(`take-quiz/save/`, {
            selected_answer: this.answer,
            question: question,
            quiz: quizid,
          })
        );
      console.log(res);
    },
    nextQuestion() {
      this.saveQuestion();
      if (this.curr == this.max) return;
      this.$router.push({
        path: '/quizsolve',
        query: { quizid: this.quizID, question: this.curr + 1 },
      });
    },
    prevQuestion() {
      this.saveQuestion();
      if (this.curr == 1) return;
      this.$router.push({
        path: '/quizsolve',
        query: { quizid: this.quizID, question: this.curr - 1 },
      });
    },
    submitAnswer() {
      this.completed = true;
    },
  },
};
</script>
