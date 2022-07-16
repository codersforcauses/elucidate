<template>
  <button
    :class="`inline-flex rounded-full shadow-sm 
    ${'bg-' + colour} 
    text-${textColour} font-bold px-7 py-1`"
  >
    <slot />
  </button>
</template>

<script>
import Color from 'color';
export default {
  name: 'QuizButton',
  props: {
    colour: {
      type: String,
      default: 'red',
    },
  },
  data() {
    return {
      // Display white text on dark backgrounds & vice-versa
      textColour: 'white',
    };
  },
  mounted() {
    // Get the class background colour via the final colour
    const buttonColour = window
      .getComputedStyle(this.$el)
      .getPropertyValue('background-color');

    if (Color(buttonColour).isLight()) {
      return 'black';
    } else {
      return 'white';
    }
  },
};
</script>
