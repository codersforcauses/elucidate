<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <QuizInput fieldName="Subject" :shadowOn="true">
        <multiselect
          v-model="subjectValue"
          :options="subjectOptions"
          placeholder="Search or select a subject"
          class="beginQuizSelector"
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
          :hide-selected="true"
          placeholder="Search or select topics"
          class="rounded-lg beginQuizSelector"
        >
        </multiselect>
      </QuizInput>
      <QuizInput fieldName="Number of Questions" :shadowOn="true">
        <input
          v-model="numOfQuestion"
          placeholder="Enter number of questions"
          type="number"
          min="1"
          class="w-full p-2 rounded-lg"
        />
      </QuizInput>
      <QuizInput fieldName="Type of Questions" :shadowOn="false">
        <div class="flex">
          <SelectBox label="Multiple Choice" />
          <SelectBox label="Short Answer" />
          <SelectBox label="Long Answer" />
        </div>
      </QuizInput>
    </div>
    <div class="flex justify-between">
      <button
        class="rounded-full hover:font-bold bg-red2 hover:bg-red hover:text-white shadow-lg py-2 px-12 mb-7"
      >
        Start Quiz
      </button>
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
    SelectBox,
  },
  layout: 'quizbg',
  data: () => ({
    numOfQuestion: '',
    subjectValue: '',
    topicValue: [],
    subjectOptions: ['Maths', 'Geography', 'Physics'],
    topicOptions: ['Differentiation', 'Trigonometry', 'Integration'],
  }),
  methods: {},
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
.beginQuizSelector .multiselect__tag,
.beginQuizSelector .multiselect__option--highlight,
.beginQuizSelector .multiselect__option--highlight::after {
  background-color: #fcd47c;
  color: black;
}

.beginQuizSelector .multiselect__tag i:hover {
  background-color: #d19a24;
  color: black;
}

.beginQuizSelector .multiselect__tags {
  border-radius: 6px;
  font-size: 16px;
  border-width: 0px;
}
.beginQuizSelector .multiselect__placeholder {
  margin-bottom: 0px;
  padding-top: 0px;
}
</style>
