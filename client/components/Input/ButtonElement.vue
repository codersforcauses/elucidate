<template>
  <nuxt-link v-if="to !== undefined" :to="to">
    <button
      v-if="type === 'primary'"
      :type="submitType"
      :class="`bg-white border-solid text-pink-600 border-pink-600 border-2 ${commonBtnStyles}`"
    >
      <slot></slot>
    </button>

    <button
      v-else
      :class="`bg-white text-primary border border-solid border-primary ${commonBtnStyles}`"
    >
      <slot></slot>
    </button>
  </nuxt-link>
  <span v-else>
    <button
      v-if="type === 'primary'"
      :class="`bg-white border-solid text-pink-600 border-pink-600 border-2 ${commonBtnStyles}`"
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
    submitType: {
      type: String,
      default: undefined,
    },
    to: {
      type: String,
      default: undefined,
    },
    type: {
      type: String,
      default: 'primary',
    },
  },
  data: () => ({
    commonBtnStyles:
      'h-10 w-40 rounded-md hover:shadow-lg transition-shadow duration-200 ease-in-out content-center',
  }),
};
</script>
