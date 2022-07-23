<template>
  <div
    class="w-full border-lightgrey/75 border rounded-md py-2 px-6 mr-5 grid-cols-7 grid"
    @click="$emit('showQuiz', quiz)"
  >
    <div class="col-span-2">{{ quiz.name }}</div>
    <div class="flex w-full space-x-2 col-span-2">
      <QuizTag
        v-for="(tag, index) in quiz.tags"
        :key="index"
        :label="tag.name"
        :colour="tag.color"
      />
    </div>
    <div class="col-span-2">{{ Date(quiz.dateCreated).slice(0, 21) }}</div>
    <div>{{ quiz.score ? quiz.score + '%' : `Not Taken` }}</div>
  </div>
</template>

<script>
export default {
  name: 'QuizListItem',
  props: {
    quiz: {
      type: Object,
      default: () => ({
        name: '',
        tags: [],
        dateCreated: '',
      }),
    },
  },
};
</script>
