<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-row h-64">
      <div>
        <h2 class="text-white my-5">Subject:</h2>
        <div class="bg-white w-50 h-5 my-5"></div>
      </div>
      <div></div>
      <div></div>
      <div></div>
    </div>
    <div class="flex justify-between mt-auto">
      <div class="w-10">Button</div>
    </div>
  </ContentBox>
</template>

<script>
import ContentBox from '~/components/Quiz/ContentBox.vue';

export default {
  name: 'beginquiz',
  layout: 'quizbg',
  components: {
    ContentBox
  }
};
</script>