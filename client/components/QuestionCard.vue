<template>
  <div class="relative w-128 pb-4 bg-violet-300 rounded-sm shadow-md">
    <!-- Question Number -->
    <div class="bg-teal-100 py-4 rounded-sm">
        <h1 class="text-center">
            Question Numb
            <ProgressBar/>
        </h1>
    </div>
    <!-- Question Detail -->
    <div class="">
        <div class="justify-self-start text-sm">
            Question Details 
            ALorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
        </div> 
    </div>

    <!-- Next/Back buttons -->
    <div class="flex justify-end px-5 mt-2">
      <button>
        <div class="inline-block text-center text-xs text-white py-0.5 px-2 mr-1 bg-yellow-600 rounded-xl shadow-md hover:bg-yellow-700 hover:shadow-lg focus:bg-yellow-700 focus:shadow-lg focus:outline-none active:bg-yellow-800 active:shadow-lg transition duration-300 ease-in-out">
            Back
        </div>
      </button>
      <button>
        <div class="inline-block text-center text-xs text-white py-0.5 px-2 bg-pink-600 rounded-xl shadow-md hover:bg-pink-700 hover:shadow-lg focus:bg-pink-700 focus:shadow-lg focus:outline-none active:bg-pink-800 active:shadow-lg transition duration-300 ease-in-out">
            Next
        </div>
      </button>
    </div>

  </div>
</template>

<script>
export default {
    name: "QuestionCard",
    data: function () {
        return {
            quizID: "num"
        };
    },
    components: { ProgressBar }
};

import ProgressBar from './ProgressBar.vue';
</script>