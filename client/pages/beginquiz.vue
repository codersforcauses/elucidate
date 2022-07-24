<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Subject:</h2>
        <div class="w-2/3 mx-5 rounded-lg shadow-lg">
          <multiselect
            v-model="subjectValue"
            :options="subjectOptions"
            placeholder="Search or select a subject"
          ></multiselect>
        </div>
      </div>
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Topic:</h2>
        <!-- <div class="bg-white w-2/3 h-auto mx-5 p-2 rounded-lg shadow-lg"> -->
        <div class="w-2/3 mx-5 rounded-lg shadow-lg">
          <multiselect
            v-model="topicValue"
            :options="topicOptions"
            :multiple="true"
            :close-on-select="false"
            :clear-on-select="false"
            :preserve-search="true"
            :hide-selected="true"
            placeholder="Search or select topics"
          >
          </multiselect>
        </div>
      </div>
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Number of Questions:</h2>
        <div class="bg-white w-2/3 h-auto mx-5 p-2 rounded-lg shadow-lg">
          <div>
            <vue-numeric-input
              v-model="numOfQuestion"
              :step="1"
            ></vue-numeric-input>
          </div>
        </div>
      </div>
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Question Type:</h2>
        <div class="flex flex-row justify-between w-2/3 h-auto mx-5 p-2">
          <div class="flex items-center mx-2 w-auto">
            <div
              class="bg-green2 rounded-lg shadow-lg hover:bg-red2 hover:text-white"
            >
              <p class="select-none m-2">Multiple Choice</p>
            </div>
          </div>
          <div class="flex items-center mx-2 w-auto">
            <div
              class="bg-green2 rounded-lg shadow-lg hover:bg-red2 hover:text-white"
            >
              <p class="select-none m-2">Short Answer</p>
            </div>
          </div>
          <div class="flex items-center mx-2 w-auto">
            <div
              class="bg-green2 rounded-lg shadow-lg hover:bg-red2 hover:text-white"
            >
              <p class="select-none m-2">Long Answer</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-between mt-auto">
      <button class="bg-red2 rounded-lg shadow-lg py-2 px-4">Start Quiz</button>
    </div>
  </ContentBox>
</template>

<script>

import Multiselect from 'vue-multiselect';
import VueNumericInput from 'vue-numeric-input';
import ContentBox from '~/components/Quiz/ContentBox.vue';

export default {
  name: 'BeginQuiz',

  components: {
    ContentBox,
    Multiselect,
    VueNumericInput
  },
  layout: 'quizbg',
  data: () => ({
    numOfQuestion: 0,
    subjectValue: '',
    topicValue: [],
    subjectOptions: ['Math', 'Geography', 'Physic'],
    topicOptions: ['Calculus', 'Trigonometry', 'Logarithm'],
  }),
  methods: {
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
