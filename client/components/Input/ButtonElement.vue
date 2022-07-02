<template>
  <span>
    <button
      v-if="type === 'primary'"
      :class="'text-white bg-primary ' + commonCSS"
    >
      <slot></slot>
    </button>

    <button
      v-else
      :class="
        'bg-white text-primary border border-solid border-primary ' + commonCSS
      "
    >
      <slot></slot>
    </button>
  </span>
</template>

<script>
export default {
  name: 'ButtonElement',
  data: () => ({
    commonCSS: 'h-10 w-32 rounded-md',
  }),
  props: {
    type: {
      type: String,
      default: 'primary',
    },
  },
};
</script>

<style></style>
