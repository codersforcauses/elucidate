<template>
  <div class="h-full w-full">
    <div class="grid grid-rows-auto mr-10 space-y-2">
      <!-- 7 cols, two per property, one for score -->
      <div class="py-1 px-6 grid grid-cols-7 text-lightgrey font-bold">
        <h1 class="col-span-2">Title</h1>
        <h1 class="col-span-2">Tags</h1>
        <h1 class="col-span-2">Date Taken</h1>
        <h1>Your Score</h1>
      </div>
      <QuizListItem
        v-for="(quiz, index) in quizzes"
        :key="index"
        :quiz="quiz"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuizList',
  props: {
    quizzes: {
      type: Array,
      default: null,
    },
  },
  data: () => ({
    listItemStyles: 'h-10 my-4 p-10',
  }),
  methods: {},
};
</script>
