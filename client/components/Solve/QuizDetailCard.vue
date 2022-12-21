<template>
  <div class="relative w-80">
    <div class="ml-12 pb-4 bg-indigo-300 rounded-sm shadow-md">
      <!-- Quiz Name -->
      <div class="bg-teal-100 py-4 rounded-sm">
        <h1 class="text-center">{{ quizName }}</h1>
      </div>
      <!-- Subject/Topic Name -->
      <div
        class="absolute top-11 inset-x-9 ml-11 bg-white rounded-sm shadow-md"
      >
        <p class="text-center">{{ topicName }}</p>
      </div>
      <!-- Questions and time -->
      <div class="grid grid-cols-2 pt-5 px-9">
        <div class="justify-self-start text-sm">{{ totalQues }} Questions</div>
        <div class="justify-self-end text-sm">{{ time }}</div>
      </div>
      <!-- Objectives
      <div class="pt-5 px-9">
        <div
          class="inline-block text-sm bg-white px-2 mb-2 rounded-sm shadow-md"
        >
          Objectives:
        </div>
        <div v-for="aim in aimList" :key="aim.content" class="pl-2">
          <div class="flex text-xs pb-1">
            <div class="w-6"><img v-bind:src="pointImg" /></div>
            <div>{{ aim.content }}</div>
          </div>
        </div>
      </div> -->
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
    </div>

    <!-- <div class="absolute top-16">
      <CountdownTimer />
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'QuizDetailCard',
  props: ['topicName', 'totalQues'],
  data: function () {
    return {
      quizName: 'Quiz Name',
      pointImg: require('~/assets/point.svg'),
      time: '1 hour',
    };
  },
};
</script>
