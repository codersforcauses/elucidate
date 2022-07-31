<template>
  <div>
    <button
      :class="`inline-flex rounded-full shadow-sm 
      ${colour} ${textColour} 
      font-bold px-7 py-1`"
    >
      <slot />
    </button>
  </div>
</template>

<script>
import Color from 'color';
export default {
  name: 'QuizButton',
  props: {
    colour: {
      type: String,
      default: 'bg-red',
      validator(v) {
        return v.startsWith('bg-');
      },
    },
  },
  data() {
    return {
      // Display white text on dark backgrounds & vice-versa
      textColour: 'text-white',
    };
  },
  mounted() {
    // Get the class background colour via the final colour
    const buttonColour = window
      .getComputedStyle(this.$el)
      .getPropertyValue('background-color');

    if (Color(buttonColour).isLight()) {
      this.textColour = 'text-black';
    } else {
      this.textColour = 'text-white';
    }
  },
};
</script>
