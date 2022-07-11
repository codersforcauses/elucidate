<template>
  <span>
    <button
      v-if="type === 'primary'"
      :class="`text-white bg-primary ${commonBtnStyles}`"
    >
      <slot></slot>
    </button>

    <button
      v-else
      :class="`bg-white text-primary border border-solid border-primary ${commonBtnStyles}`"
    >
      <slot></slot>
    </button>
  </span>
</template>

<script>
export default {
  name: 'ButtonElement',
  props: {
    type: {
      type: String,
      default: 'primary',
    },
  },
  data: () => ({
    commonBtnStyles:
      'h-10 w-32 rounded-md hover:shadow-lg transition-shadow duration-200 ease-in-out',
  }),
};
</script>
