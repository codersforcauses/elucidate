<template>
  <button
    type="submit"
    :class="
      disabled
        ? 'text-darkgrey bg-lightgrey border-darkgrey'
        : 'text-red bg-white border-red'
    "
    class="place-self-center text-l font-bold h-8 px-2 rounded border border-solid my-5"
    :disabled="disabled"
  >
    <slot />
  </button>
</template>

<script>
export default {
  name: 'AuthSubmit',
  props: {
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
