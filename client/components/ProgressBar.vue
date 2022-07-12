<script>

  export default {
    data() {
      return {
        // curr:1,
        // max:20
      }
    },
    // methods: {
    //   clicked() {
    //     curr = Math.random() * max
    //   }
    // },
    props: [
      'curr',
      'max'
    ]
  }
</script>

<template>
  <div class="w-full bg-gray-300 rounded-full h-2.5 dark:bg-gray-300">
    <div class="bg-yellow-600 h-2.5 rounded-full" :style="{width: `${(curr / max) * 100}%`}"></div>
  </div>
</template>