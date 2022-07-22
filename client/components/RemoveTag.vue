<template>
  <div class="relative m-1.5">
    <div v-bind:class="{bg: colour}">{{ label }}</div>
    <button @click="$emit('toggleTag', label)" class="relative left-[188px]">x</button>
  </div>
</template>

<script>
export default {
  props: ['label', 'colour'],
};
</script>

<style>
</style>