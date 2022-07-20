<template>
  <div class="h-[15.5rem] w-[15.75rem] hover:shadow-lg transition-shadow duration-200 ease-in-out">
    <div class="flex flex-col space-y-2 justify-center items-center bg-lightgrey/75 h-full">
      <div v-if="color === 'green'" :class="`bg-green ${commonColoredBoxStyles}`">
        {{value}}
      </div>
      <div v-if="color === 'yellow'" :class="`bg-yellow ${commonColoredBoxStyles}`">
        {{value}}
      </div>
      <div v-if="color === 'red'" :class="`bg-red ${commonColoredBoxStyles}`">
        {{value}}
      </div>
      <div>
        <p class="text-lg font-medium">
          {{label}}
        </p>
      </div>

      <!-- <div @click="$emit('SelectAttri', label)"> -->
      <ButtonElement @buttonClicked="$emit('SelectAttri', label)" type="tertiary"> 
        {{buttonLabel}}
      </ButtonElement>
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
import ButtonElement from '../Input/ButtonElement.vue';
export default {
  components: { ButtonElement },
  name: 'UserAttributeCard',
  data: () => ({
    commonColoredBoxStyles:
      'rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center',
  }),
  props: {
    label: {
      type: String,
      default: undefined,
    },
    buttonLabel: {
      type: String,
      default: undefined,
    },
    value: {
      type: Number,
      default: 0,
    },
    color: {
      type: String,
      default: "green",
    }
  }
};
</script>