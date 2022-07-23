<template>
  <!-- container for modal, covers whole screen -->
  <div @click="closeModal()" class="py-24 px-40 fixed flex justify-center bg-darkgrey/25 inset-0">
    <!-- modal, stops click propagation -->
    <div @click.stop="" class="p-16 flex flex-row bg-white rounded-3xl h-full w-full shadow-2xl">

      <div class="flex flex-col w-1/3">
        <h1 class="font-extrabold text-4xl">{{quiz.name}}</h1>
        <h2 class="text-lg font-extrathin">Created By - {{quiz.author}}</h2>
        <div class="flex-1 grid grid-rows-3 grid-cols-2 text-center items-center">
          <!-- hard coded for now. -->
            <ColouredBox color="green" value="42"/> <p>Average Quiz Result</p>
            <ColouredBox color="red" value="42"/> <p>Users Attempted</p>
            <ColouredBox color="blue" value="42"/> <p>Questions</p>

        </div>
        <p>Created on {{Date(quiz.dateCreated).slice(0, 21)}} </p>
      </div>

      <div class="w-2/3">
        <div class="justify-right items-right text-right">
          <h1 class="font-extrabold text-xl text-right">Tags/Subjects</h1>
          <QuizTag
            v-for="(tag, index) in quiz.tags"
            :key="index"
            :label="tag.name"
            :colour="tag.color"
          />
        </div>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In a faucibus elit. Nulla quis ultrices nunc, ut feugiat nisl. Sed ac lorem mattis ex condimentum ultrices mollis non urna. Aenean orci lacus, ultricies quis viverra porttitor, aliquam ut elit. Morbi eleifend ac magna suscipit venenatis. Mauris vitae posuere eros. Ut feugiat tempus neque, quis aliquet arcu dapibus sed. Fusce suscipit tincidunt laoreet. Cras laoreet venenatis erat laoreet dapibus. Quisque urna tortor, condimentum at mattis quis, dignissim sit amet leo.</p>
        <ButtonElement to="/Start-Quiz" type="tertiary">Start Quiz Now</ButtonElement>
      </div>

    </div>
    <div class="close">
    </div>
  </div>
</template>

<script>
import ButtonElement from '../Input/ButtonElement.vue';
import QuizTag from './QuizTag.vue';
import ColouredBox from './ColouredBox.vue'
export default {
  components: { ButtonElement, QuizTag, ColouredBox },
  name: 'QuizCard',
  props: {
    quiz: {
      name: 'asdf',
      tags: [],
      author: '',
      dateCreated: '',
    },
  },
  methods: {
    closeModal() {
       this.$emit("closeQuiz")
    }
  }
};
</script>
