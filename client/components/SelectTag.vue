<template>
  <div>
    <button :class="css" @click="$emit('toggleTag', label)">{{ label }}</button>
  </div>
</template>

<script>
export default {
  props: ['label', 'colour'],
  computed: {
    css: function () {
      return this.colour + ' rounded';
    },
  },
};
</script>

<style scoped></style>
