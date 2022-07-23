<template>
  <div class="flex flex-col w-2/3 mx-auto shadow-lg">
    <div class="bg-green2 shadow-lg">
      <h2 class="m-5 font-bold">{{ title }}</h2>
    </div>
    <div class="flex flex-col items-center bg-blue2">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContentBox',
  props: {
    title: String,
  }
};
</script>