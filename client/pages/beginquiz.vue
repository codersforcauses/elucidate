<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <QuizInput field-name="Subject" :shadow-on="true">
        <MultiselectBox
          ref="selectedSubject"
          :options="subjectOptions"
          placeholder="Search or select a subject"
        ></MultiselectBox>
      </QuizInput>
      <QuizInput field-name="Topics" :shadow-on="true">
        <MultiselectBox
          ref="selectedTopics"
          :options="topicOptions"
          placeholder="Search or select topics"
          :multiple="true"
          :hide-selected="true"
        ></MultiselectBox>
      </QuizInput>
      <QuizInput field-name="Number of Questions" :shadow-on="true">
        <input
          v-model="numOfQuestion"
          placeholder="Enter number of questions"
          type="number"
          min="1"
          class="w-full p-2 rounded-lg"
        />
      </QuizInput>
      <QuizInput field-name="Type of Questions" :shadow-on="false">
        <div class="flex">
          <SelectBox ref="multipleChoice" label="Multiple Choice" />
          <SelectBox ref="shortAnswer" label="Short Answer" />
          <SelectBox ref="longAnswer" label="Long Answer" />
        </div>
      </QuizInput>
    </div>
    <div class="flex justify-between">
      <button
        class="rounded-full hover:font-bold bg-red2 hover:bg-red hover:text-white shadow-lg py-2 px-12 mb-7"
        @click="getValues"
      >
        Start Quiz
      </button>
      <button
        class="rounded-full hover:font-bold bg-red2 hover:bg-red hover:text-white shadow-lg py-2 px-12 mb-7"
        @click="changeOptions"
      >
        change
      </button>
    </div>
  </ContentBox>
</template>

<script>
import MultiselectBox from '~/components/Quiz/MultiselectBox.vue';
import ContentBox from '~/components/Quiz/ContentBox.vue';
import QuizInput from '~/components/Quiz/QuizInput.vue';
import SelectBox from '~/components/Quiz/SelectBox.vue';

export default {
  name: 'BeginQuiz',
  components: {
    ContentBox,
    MultiselectBox,
    QuizInput,
    SelectBox,
  },
  layout: 'quizbg',
  data: () => ({
    numOfQuestion: '',
    subjectOptions: ['Maths', 'Geography', 'Physics'],
    topicOptions: ['Differentiation', 'Trigonometry', 'Integration'],
    allOptions: {
      Maths: [
        'Maths - Differentiation',
        'Maths - Trigonometry',
        'Maths - Integration',
      ],
      Physics: ['Physics - Motion', 'Physics - Force', 'Physics - Planet'],
      Geography: [
        'Geography - GPS',
        'Geography - Country',
        'Geography - Culture',
      ],
    },
  }),
  methods: {
    changeOptions() {
      this.topicOptions = this.allOptions[this.$refs.selectedSubject.value];
    },
    getValues() {
      const allValues = [];
      allValues.push(this.$refs.selectedSubject.value);
      allValues.push(this.$refs.selectedTopics.value);
      allValues.push(this.numOfQuestion);
      allValues.push(this.$refs.multipleChoice.isSelected);
      allValues.push(this.$refs.shortAnswer.isSelected);
      allValues.push(this.$refs.longAnswer.isSelected);
      console.log(allValues);
    },
  },
};
</script>
