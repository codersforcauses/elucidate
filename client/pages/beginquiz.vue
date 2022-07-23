<template>
  <ContentBox class="flex justify-center" title="Begin Quiz">
    <div class="flex flex-col my-10 w-full h-auto">
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Subject:</h2>
        <div class="bg-white w-2/3 h-auto mx-5 p-2 rounded-lg shadow-lg">Maths</div>
      </div>
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Topic:</h2>
        <div class="bg-white w-2/3 h-auto mx-5 p-2 rounded-lg shadow-lg">Calculus</div>
      </div>
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Number of Questions:</h2>
        <div class="bg-white w-2/3 h-auto mx-5 p-2 rounded-lg shadow-lg">3</div>
      </div>
      <div class="flex flex-row justify-between items-center w-full h-15 my-5">
        <h2 class="text-white w-1/4 mx-5">Question Type:</h2>
        <div class="flex flex-row justify-between w-2/3 h-auto mx-5 p-2">
          <div class="flex items-center mx-2 w-auto">
            <div class="bg-green2 rounded-lg shadow-lg hover:bg-red2 hover:text-white">
              <p class="select-none m-2">Multiple Choice</p>
            </div>
          </div>
          <div class="flex items-center mx-2 w-auto">
            <div class="bg-green2 rounded-lg shadow-lg hover:bg-red2 hover:text-white">
              <p class="select-none m-2">Short Answer</p>
            </div>
          </div>
          <div class="flex items-center mx-2 w-auto">
            <div class="bg-green2 rounded-lg shadow-lg hover:bg-red2 hover:text-white">
              <p class="select-none m-2">Long Answer</p>
            </div>
          </div>
        </div>
      </div>
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