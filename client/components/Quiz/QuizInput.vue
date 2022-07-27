<template>
  <div class="flex flex-row justify-between items-center w-full h-15 my-5">
    <h2 class="text-white w-1/4 mx-5 font-bold">{{ fieldName }}:</h2>
    <div class="w-2/3 mx-5 rounded-lg" :class="shadowOn ? 'shadow-lg' : ''">
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
  }
};
</script>