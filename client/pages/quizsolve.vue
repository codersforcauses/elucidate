<template>
  <div class="flex m-20">
    <div>
      <QuizDetailCard />
    </div>
    <div class="ml-10 min-w-[50%] min-h-[40%]">
      <QuestionCard />
    </div>
  </div>
  <!-- <ProgressBar></ProgressBar> -->
</template>

<script>
export default {
  name: 'quizSolve',
};
</script>
