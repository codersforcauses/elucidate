<template>
  <div
    class="w-full border-lightgrey/75 border rounded-md py-2 px-6 mr-5 grid-cols-9 grid"
  >
    <div class="col-span-2">{{ Quiz.name }}</div>
    <div class="flex w-full col-span-2">
      <QuizTag
        v-for="(tag, index) in Quiz.tags"
        :key="index"
        :label="tag.name"
        :colour="tag.color"
      />
    </div>
    <div class="col-span-2">{{ Quiz.author }}</div>
    <div class="col-span-2">{{ Date(Quiz.dateCreated).slice(0, 21) }}</div>
    <div>{{ Quiz.score ? Quiz.score + '%' : `Not Taken` }}</div>
  </div>
</template>

<script>
import QuizTag from './QuizTag.vue';
export default {
  name: 'QuizListItem',
  props: {
    Quiz: {
      name: '',
      tags: [],
      author: '',
      dateCreated: '',
    },
  },
};
</script>
