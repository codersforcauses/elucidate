<template>
  <div class="relative mx-1.5">
    <button @click="$emit('toggleTag', label)" :class=css>{{ label }}</button>
  </div>
</template>

<script>
export default {
  name: 'QuizTag',
  computed: {
    css : function () {
      return "bg-" + this.colour + " rounded px-2";
    }
  },
  props: ['label', 'colour']
}
</script>

<style>
</style>