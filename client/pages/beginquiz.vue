<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <QuizInput fieldName="Subject" :shadowOn="true">
          <multiselect
            v-model="subjectValue"
            :options="subjectOptions"
            placeholder="Search or select a subject"
          ></multiselect>
      </QuizInput>
      <QuizInput fieldName="Topics" :shadowOn="true">
        <multiselect
          v-model="topicValue"
          :options="topicOptions"
          :multiple="true"
          :close-on-select="true"
          :clear-on-select="false"
          :preserve-search="true"
          :hide-selected="false"
          placeholder="Search or select topics"
          class="rounded-lg"
        >
        </multiselect>
      </QuizInput>
      <QuizInput fieldName="Number of Questions" :shadowOn="true">
        <input v-model="numOfQuestion" placeholder='Enter number of questions' type="number" min="1" class= "w-full p-2 rounded-lg">
      </QuizInput>
      <QuizInput fieldName="Type of Questions" :shadowOn="false">
        <div class="flex justify-between">
          <SelectBox label="Multiple Choice" />
          <SelectBox label="Short Answer" />
          <SelectBox label="Long Answer" />
        </div>
      </QuizInput>
    </div>
    <div class="flex justify-between mb-4">
      <button class="bg-red2 hover:bg-red hover:text-white rounded-lg shadow-lg py-2 px-4">Start Quiz</button>
    </div>
  </ContentBox>
</template>

<script>

import Multiselect from 'vue-multiselect';
import ContentBox from '~/components/Quiz/ContentBox.vue';
import QuizInput from '~/components/Quiz/QuizInput.vue';
import SelectBox from '~/components/Quiz/SelectBox.vue';

export default {
  name: 'BeginQuiz',
  components: {
    ContentBox,
    Multiselect,
    QuizInput,
    SelectBox
  },
  layout: 'quizbg',
  data: () => ({
    numOfQuestion: '',
    subjectValue: '',
    topicValue: [],
    subjectOptions: ['Maths', 'Geography', 'Physics'],
    topicOptions: ['Differentiation', 'Trigonometry', 'Integration'],
  }),
  methods: {
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
  .multiselect__tags{
  border-radius:6px;
  font-size:16px;
  border-width:0px;
  }
  .multiselect__placeholder{
  margin-bottom: 0px;
  padding-top:0px;
  }
</style>
