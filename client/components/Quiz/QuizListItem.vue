<template>
  <div class="w-full border-lightgrey/75 border rounded-md py-2 px-6 mr-5 grid-cols-4 grid">
    <div>{{Quiz.name}}</div>
    <div class="flex w-full">
      <QuizTag v-for="(tag, index) in Quiz.tags" :key="index" :label="tag.name" :colour="tag.color" />
    </div>
    <div>{{Quiz.author}}</div>
    <div>{{Quiz.dateCreated}}</div>
       
  </div>
</template>

<script>
import QuizTag from './QuizTag.vue'
export default {
  name: 'QuizListItem',
  props: {
    Quiz: {
      name: '',
      tags: [],
      author: '',
      dateCreated: '',
    }
  }
};
</script>
