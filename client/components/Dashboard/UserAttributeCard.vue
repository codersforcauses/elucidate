<template>
  <div class="h-64 w-64 hover:shadow-lg transition-shadow duration-200 ease-in-out">
    <div class="flex flex-col space-y-3 justify-center items-center bg-lightgrey/75 h-full">
      <div v-if="color === 'green'" class="bg-green rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center">
        {{propertyValue}}
      </div>
      <div v-if="color === 'yellow'" class="bg-yellow rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center">
        {{propertyValue}}
      </div>
      <div v-if="color === 'red'" class="bg-red rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center">
        {{propertyValue}}
      </div>
      <div>
        <p class="text-xl font-medium">
          {{property}}
        </p>
      </div>
      <ButtonElement type="tertiary"> 
        View Quizzes
      </ButtonElement>
    </div>
  </div>
</template>

<script>
import ButtonElement from '../Input/ButtonElement.vue';
export default {
  components: { ButtonElement },
  name: 'UserAttributeCard',
  props: {
    property: {
      type: String,
      default: undefined,
    },
    propertyValue: {
      type: String,
      default: undefined,
    },
    color: {
      type: String,
      // default: "green",
    }
  }
};
</script>