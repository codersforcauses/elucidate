<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <InputLabel field-name="Subject" :shadow-on="true">
        <MultiselectBox
          ref="selectedSubject"
          :options="Object.keys(allOptions)"
          placeholder="Search or select a subject"
          @getData="updateSubject($event)"
        ></MultiselectBox>
      </InputLabel>
      <InputLabel field-name="Topics" :shadow-on="true">
        <MultiselectBox
          ref="choosenTopics"
          :options="selectedSubject ? allOptions[selectedSubject] : []"
          placeholder="Search or select topics"
          :multiple="true"
          :hide-selected="true"
          :allow-empty="true"
          @getData="(selectedTopics = $event), checkValidity()"
        ></MultiselectBox>
      </InputLabel>
      <InputLabel field-name="Number of Questions" :shadow-on="true">
        <input
          v-model="numOfQuestion"
          placeholder="Enter number of questions"
          type="number"
          min="1"
          oninput="validity.valid||(value='')"
          class="w-full p-2 rounded-lg"
          @input="checkValidity()"
        />
      </InputLabel>
      <InputLabel field-name="Type of Questions" :shadow-on="false">
        <div class="flex">
          <SelectBox
            ref="multipleChoice"
            label="Multiple Choice"
            @getData="(multChoiceSelected = $event), checkValidity()"
          />
          <SelectBox
            ref="shortAnswer"
            label="Short Answer"
            @getData="(shortAnswerSelected = $event), checkValidity()"
          />
          <SelectBox
            ref="longAnswer"
            label="Numeric"
            @getData="(numericSelected = $event), checkValidity()"
          />
        </div>
      </InputLabel>
    </div>
    <div class="flex justify-between">
      <button
        :disabled="!validData"
        class="rounded-full shadow-lg py-2 px-12 mb-7"
        :class="
          validData
            ? 'hover:font-bold bg-red2 hover:bg-red hover:text-white'
            : 'text-darkgrey bg-lightgrey'
        "
        @click="getValues"
      >
        Start Quiz
      </button>
    </div>
  </ContentBox>
</template>

<script>
import MultiselectBox from '~/components/Quiz/MultiselectBox.vue';
import ContentBox from '~/components/Quiz/ContentBox.vue';
import InputLabel from '~/components/Quiz/InputLabel.vue';
import SelectBox from '~/components/Quiz/SelectBox.vue';

export default {
  name: 'BeginQuiz',
  components: {
    ContentBox,
    MultiselectBox,
    SelectBox,
    InputLabel,
  },
  layout: 'quizbg',
  data: () => ({
    numOfQuestion: '',
    selectedSubject: '',
    selectedTopics: [],
    validData: false,
    multChoiceSelected: false,
    shortAnswerSelected: false,
    numericSelected: false,
    // Hardcoded options, need fetch data from backend
    allOptions: {
      Maths: ['Differentiation', 'Trigonometry', 'Integration'],
      Physics: ['Motion', 'Force', 'Planet'],
      Geography: ['GPS', 'Country', 'Culture'],
    },
  }),
  methods: {
    updateSubject(selectedSubject) {
      this.selectedSubject = selectedSubject;
      this.$refs.choosenTopics.value = [];
    },
    checkValidity() {
      const quesTypeSelected =
        this.multChoiceSelected ||
        this.shortAnswerSelected ||
        this.numericSelected;
      if (
        this.selectedTopics.length > 0 &&
        this.numOfQuestion &&
        quesTypeSelected
      ) {
        this.validData = true;
      } else {
        this.validData = false;
      }
    },
    getValues() {
      // Need to send data to backend
    },
  },
};
</script>

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
