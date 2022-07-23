<template>
  <div class="">
    <button :class="css">{{ label }}</button>
  </div>
</template>

<script>
export default {
  name: 'QuizTag',
  props: {
    'label': {
      type: String,
      default: undefined,
    },
    'colour': {
      type: String,
      default: 'blue',
    },
  },
  computed: {
    css: function () {
      return 'bg-' + this.colour + ' rounded px-2';
    },
  },
  
}
</script>
