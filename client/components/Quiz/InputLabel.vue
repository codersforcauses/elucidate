<template>
  <div class="flex flex-row justify-centre items-center w-full h-15 my-5">
    <label class="flex align-text-top text-white text-xl font-bold">
      {{ fieldName }}
    </label>
    <div class="w-full mx-5 rounded-lg" :class="shadowOn ? 'shadow-lg' : ''">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuizInput',
  props: {
    fieldName: String,
    shadowOn: Boolean,
  },
};
</script>
