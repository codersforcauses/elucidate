<template>
  <div>
    <div class="flex flex-col my-10">
      <Box title="Create a Question" :is-centered="false">
        <div class="inline-flex mt-10 mx-20">
          <InputLabel field-name="Types: ">
            <div
              class="inline-flex gap-2 ml-[100px] text-white text-md font-bold"
            >
              <button class="bg-yellow rounded-full shadow-md px-5 py-3">
                Multiple Choice
              </button>
              <button class="bg-blue rounded-full shadow-md px-5 py-3">
                Short Answer
              </button>
              <button class="bg-red rounded-full shadow-md px-5 py-3">
                Numeric Question
              </button>
            </div>
          </InputLabel>
        </div>

        <div>
          <InputLabel class="ml-[70px]" field-name="Subjects: ">
            <MultiselectBox
              ref="selectedSubject"
              class="flex flex-row ml-[18px] w-[700px] justify-centre items-center shadow-md"
              :options="subjectOptions"
              placeholder="Search or select a subject"
            ></MultiselectBox>
          </InputLabel>
        </div>
        <div>
          <InputLabel class="ml-[80px]" field-name="Topics: ">
            <MultiselectBox
              ref="selectedTopics"
              class="flex flex-row ml-[30px] w-[700px] justify-centre items-center shadow-md"
              :options="topicOptions"
              placeholder="Search or select topics"
              :multiple="true"
              :hide-selected="true"
            ></MultiselectBox>
          </InputLabel>
        </div>

        <InputLabel class="ml-[60px]" field-name="Question: "
          ><QuestionBox
        /></InputLabel>

        <InputLabel class="ml-[75px]" field-name="Answer: "
          ><ResponseBox class="ml-[8px]"></ResponseBox>
        </InputLabel>

        <div class="flex place-content-end mt-5 pb-5 mx-10">
          <QuizButton color="red" class="mr-10 shadow-md">
            + Add Question
          </QuizButton>
          <QuizButton color="red" class="shadow-md">Finish</QuizButton>
        </div>
      </Box>
    </div>
  </div>
</template>

<script>
import Box from '~/components/Quiz/Box.vue';
import QuestionBox from '~/components/Quiz/QuestionBox.vue';
import ResponseBox from '~/components/Quiz/ResponseBox.vue';
import QuizButton from '~/components/Quiz/QuizButton.vue';
import MultiselectBox from '~/components/Quiz/MultiselectBox.vue';
import InputLabel from '~/components/Quiz/InputLabel.vue';

export default {
  components: {
    Box,
    QuestionBox,
    ResponseBox,
    QuizButton,
    MultiselectBox,
    InputLabel,
  },

  data: () => ({
    subjectOptions: ['Maths', 'Chemistry'],
    topicOptions: ['Differentiation', 'Calculus'],
  }),
};
</script>
