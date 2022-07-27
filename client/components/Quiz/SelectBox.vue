<template>
  <div class="flex items-center mx-2 w-auto">
    <div class="bg-green2 rounded-lg shadow-lg hover:bg-red hover:text-white">
      <p class="select-none m-2 whitespace-nowrap">{{ label }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SelectBox',
  props: {
    label: String,
  }
};
</script>