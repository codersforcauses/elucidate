<template>
  <div class="relative w-80">
    <div class="ml-12 pb-4 bg-indigo-300 rounded-sm shadow-md">
      <!-- Subject Name -->
      <div class="bg-teal-100 py-4 rounded-sm">
        <h1 class="text-center font-bold">{{ subjectName }}</h1>
      </div>

      <div class="px-5">
        <!-- Questions -->
        <div class="grid grid-cols-2 pt-5">
          <div class="justify-self-start text-sm">
            {{ totalQues }} Questions
          </div>
        </div>

        <!-- Topics -->
        <p class="mt-5 font-bold">Topics</p>
        <div class="grid grid-cols-2">
          <div
            class="justify-self-start text-sm"
            v-for="(topic, index) in topics"
            v-bind:key="index"
          >
            <div>
              {{ topic.name }}
            </div>
          </div>
        </div>

        <!-- Pause and Restart buttons 
      <div class="flex justify-end px-5 mt-2">
        <button>
          <div
            class="inline-block text-center text-xs text-white py-0.5 px-2 mr-1 bg-pink-600 rounded-xl shadow-md hover:bg-pink-700 hover:shadow-lg focus:bg-pink-700 focus:shadow-lg focus:outline-none active:bg-pink-800 active:shadow-lg transition duration-300 ease-in-out"
          >
            Pause
          </div>
        </button>
        <button>
          <div
            class="inline-block text-center text-xs text-white py-0.5 px-2 bg-teal-400 rounded-xl shadow-md hover:bg-teal-500 hover:shadow-lg focus:bg-teal-500 focus:shadow-lg focus:outline-none active:bg-teal-600 active:shadow-lg transition duration-300 ease-in-out"
          >
            Restart
          </div>
        </button>
      </div> -->

        <!-- Progress -->

        <p class="mt-5 font-bold">Progress</p>
        <div class="grid grid-cols-4 gap-2">
          <NuxtLink
            v-for="index in totalQues"
            v-bind:key="index"
            :to="`/quizsolve?quizid=${quizID}&question=${index}`"
          >
            <div
              v-if="index === curr"
              :class="
                'cursor-pointer bg-white border-2 border-solid border-black w-12 h-12 rounded-md flex items-center justify-center font-bold ' +
                (attempts.filter((c) => index === c.question).length === 0
                  ? 'bg-white'
                  : 'bg-green1')
              "
            >
              {{ index }}
            </div>
            <div
              v-else
              :class="
                'cursor-pointer border border-solid border-gray-400 w-12 h-12 rounded-md flex items-center justify-center font-bold ' +
                (attempts.filter((c) => index === c.question).length === 0
                  ? 'bg-white'
                  : 'bg-green1')
              "
            >
              {{ index }}
            </div>
          </NuxtLink>
        </div>
      </div>

      <!-- <div class="absolute top-16">
      <CountdownTimer />
    </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuizDetailCard',
  props: ['subjectName', 'topics', 'totalQues', 'quizID', 'curr', 'attempts'],
  data: function () {
    return {
      pointImg: require('~/assets/point.svg'),
    };
  },
};
</script>
