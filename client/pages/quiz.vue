<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <InputLabel field-name="Subject" :shadow-on="true">
        <MultiselectBox
          ref="selectedSubject"
          :options="Object.keys(subjects)"
          placeholder="Search or select a subject"
          @getData="updateSubject($event)"
        ></MultiselectBox>
      </InputLabel>
      <InputLabel field-name="Topics" :shadow-on="true">
        <MultiselectBox
          ref="chosenTopics"
          :options="topics.map((topic) => Object.keys(topic)[0])"
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
          placeholder="Enter number of questions (max 100)"
          type="number"
          min="1"
          max="100"
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
export default {
  name: 'QuizPage',
  components: {},
  layout: 'quizbg',
  data: () => ({
    numOfQuestion: '',
    selectedSubject: -1,
    selectedTopics: [],
    validData: false,
    multChoiceSelected: false,
    shortAnswerSelected: false,
    numericSelected: false,

    subjects: {},
    topics: [],
  }),

  async mounted() {
    // this.$auth.strategies.local.token.get();
    const res = await this.$axios.$get('quizzes/subjects/');
    // .catch((error) => {
    //   console.log(error);
    // });
    const subjectsObj = {};
    for (const subject of res.results) {
      subjectsObj[subject.name] = subject.pk;
    }

    this.subjects = subjectsObj;
  },

  methods: {
    async updateSubject(selectedSubject) {
      this.selectedSubject = this.subjects[selectedSubject];
      this.$refs.chosenTopics.value = [];

      console.log(this.selectedSubject);
      // populate chosen subject with topics
      const res = await this.$axios
        .$get('quizzes/topics/?subject=' + this.subjects[selectedSubject])
        .catch((err) => console.log(err));
      res.results.map((obj) => {
        let name = obj.name;
        let pk = obj.pk;
        this.topics.push({ [name]: pk });
      });
    },
    checkValidity() {
      const validateQuestionTypes =
        this.multChoiceSelected ||
        this.shortAnswerSelected ||
        this.numericSelected;

      const validateTopics = this.selectedTopics.length > 0;
      const validateQuestionNum =
        this.numOfQuestion > 0 && this.numOfQuestion < 100;

      if (
        validateQuestionTypes &&
        validateQuestionNum &&
        validateQuestionTypes
      ) {
        this.validData = true;
      } else {
        this.validData = false;
      }
    },
    getValues() {
      const selectedTopics = this.$refs.chosenTopics.value.map((topic) => {
        for (const obj of this.topics) {
          if (Object.keys(obj)[0] === topic) {
            return obj[topic];
          }
        }
      });
      const postData = {
        subject: this.selectedSubject,
        topics: selectedTopics,
        question_count: parseInt(this.numOfQuestion),
        question_types: {
          multiple_choice: this.multChoiceSelected,
          short_answer: this.shortAnswerSelected,
          numeric: this.numericSelected,
        },
      };

      this.$axios
        .$post('generate-quiz/generate/', postData)
        .then((res) => {
          this.$router.push({
            path: '/quiz/' + res.quiz_id,
          });
        })
        .catch((err) => console.log(err));
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
