<template>
  <div class="">
    <div v-if="color === 'green'" :class="`bg-green ${commonColoredBoxStyles}`">
      {{ value }}
    </div>

    <div
      v-if="color === 'yellow'"
      :class="`bg-yellow ${commonColoredBoxStyles}`"
    >
      {{ value }}
    </div>

    <div v-if="color === 'red'" :class="`bg-red ${commonColoredBoxStyles}`">
      {{ value }}
    </div>

    <div v-if="color === 'blue'" :class="`bg-blue ${commonColoredBoxStyles}`">
      {{ value }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'ColouredBox',
  data: () => ({
    commonColoredBoxStyles:
      'rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center',
  }),
  props: {
    value: {
      type: Number,
      default: 0,
    },
    color: {
      type: String,
      default: 'green',
    },
  },
};
</script>
