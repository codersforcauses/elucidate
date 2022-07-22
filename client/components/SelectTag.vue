<template>
  <div class="relative m-1.5">
    <button type="button" @click="$emit('toggleTag', label)" class="rounded" :class=css>{{ label }}</button>
  </div>
</template>

<script>
export default {
  computed: {
    css: function () {
      return 'bg-[#' + this.colour + ']';
    },
  },
  props: ['label', 'colour'],
};
</script>

<style>
</style>