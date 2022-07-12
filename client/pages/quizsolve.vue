<template>
  <QuestionCard />
  <!-- <ProgressBar></ProgressBar> -->
</template>

<script>
export default {
    name: "quizsolve",
    components: { QuestionCard }
};

import QuizDetailCardVue from '~/components/QuizDetailCard.vue';
import QuestionCard from '../components/QuestionCard.vue';
</script>
