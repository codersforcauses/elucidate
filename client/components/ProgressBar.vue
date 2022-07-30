<script>
export default {
  // methods: {
  //   clicked() {
  //     curr = Math.random() * max
  //   }
  // },
  props: ['curr', 'max'],
  data() {
    return {
      // curr:1,
      // max:20
    };
  },
};
</script>

<template>
  <div
    class="w-full bg-gray-300 mr-5 mt-2 bg-gray-200 rounded-full h-2.5 dark:bg-gray-300"
  >
    <div
      class="bg-yellow-600 h-2.5 rounded-full"
      :style="{ width: `${(curr / max) * 100}%` }"
    ></div>
  </div>
</template>
