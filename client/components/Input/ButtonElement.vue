<template>
  <nuxt-link v-if="to !== undefined" :to="to">
    <button
      v-if="type === 'primary'"
      :class="`text-white bg-primary ${commonBtnStyles}`"
      @click="$emit('buttonClicked')"
    >
      <slot></slot>
    </button>

    <button
      v-if="type === 'secondary'"
      :class="`bg-white text-primary border border-solid border-primary ${commonBtnStyles}`"
      @click="$emit('buttonClicked')"
    >
      <slot></slot>
    </button>

    <button
      v-if="type === 'tertiary'"
      :class="`bg-blue text-white ${thinBtnStyles}`"
      @click="$emit('buttonClicked')"
    >
      <slot></slot>
    </button>
  </nuxt-link>
  <span v-else>
    <button
      v-if="type === 'primary'"
      :class="`text-white bg-primary ${commonBtnStyles}`"
      @click="$emit('buttonClicked')"
    >
      <slot></slot>
    </button>

    <button
      v-if="type === 'secondary'"
      :class="`bg-white text-primary border border-solid border-primary ${commonBtnStyles}`"
      @click="$emit('buttonClicked')"
    >
      <slot></slot>
    </button>

    <button
      v-if="type === 'tertiary'"
      :class="`bg-blue text-white ${thinBtnStyles}`"
      @click="$emit('buttonClicked')"
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
      'h-10 w-32 rounded-md hover:shadow-lg transition-shadow duration-200 ease-in-out',
    thinBtnStyles:
      'h-6 w-40 rounded-md text-xs font-medium hover:shadow-lg transition-shadow duration-200 ease-in-out',
  }),
};
</script>
