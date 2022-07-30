<template>
    <div class="flex mx-20">
        <div>
            <QuizDetailCard
                v-if="!this.not_found"
                :topicName="this.quiz_name"
                :totalQues="this.quiz_num_questions"
            />
        </div>
        <div class="relative w-full pb-4 ml-4 bg-indigo-300 rounded-sm shadow-md min-h-full">
            <div class="flex bg-teal-100 py-4 rounded-sm">
                Quiz Review
            </div>
            <div class="flex">
                <div class="text-md bg-teal-200 w-24 h-24 rounded-lg m-5">
                    <div>Question {{ questionNum }}</div>
                    <div>Mark</div>
                </div>
                <div>
                <!-- Question Choices -->
                <div v-if="this.quizdata.question_type[0] === 'mcq'">
                    <div class="justify-center grid grid-cols-1 w-full select-none">
                    <select
                        v-model="answer"
                        multiple
                        class="overflow-hidden border-transparent focus:outline-none bg-transparent h-64"
                    >
                        <option
                        v-for="(choice, index) in this.quizdata.question_choices[
                            this.curr - 1
                        ]"
                        :key="index"
                        class="py-2 px-4 my-5 mx-20 z-50 text-center shadow-md rounded-full bg-white text-black font-sans font-semibold text-sm border-black btn-primary hover:text-gray-700 hover:bg-gray-200 focus:outline-none active:shadow-none"
                        >
                        {{ choice }}
                        </option>
                    </select>
                    <div>Selected: {{ answer }}</div>
                    <div>Answer array: {{ answerArray }}</div>
                    </div>
                </div>

                <!-- Short Answer Choices -->
                <div v-if="this.quizdata.question_type[0] === 'short_answer'">
                    <div class="p-5">
                        <div class="bg-teal-200 min-h-full p-5 rounded-sm shadow-md">
                        <div>Answer</div>
                        <textarea
                            id="message"
                            rows="4"
                            class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500"
                            placeholder="Your message..."
                        ></textarea>
                        </div>
                    </div>
                </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import dummyjson from '../components/dummy.json';
export default {
  name: 'quizReview',
  data() {
    return {
      quizID: parseInt(this.$route.query.quizid),
      quizdata: null,
      quiz_name: null,
      quiz_num_questions: null,
      not_found: false,
    };
  },
  created() {
    // TODO: Use API to process route.query.quizID

    // process dummyjson
    for (const quiz of dummyjson) {
      if (this.quizID === quiz.quiz_id) {
        this.quizdata = quiz;
        // Fill data properties
        this.quiz_name = this.quizdata.quiz_name;
        this.quiz_num_questions = 1;
        break;
      }
    }
  },
};
</script>