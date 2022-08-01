<template>
  <ul
    class="bg-red p-3 my-6 text-neutral-100 font-bold rounded-md list-disc"
  >
    <h1>
      <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
      <slot> Please fix the following errors: </slot>
    </h1>
    <li v-for="error in errors" :key="error.toString()" class="ml-8">
      <h2>{{ error.name }}</h2>
      <p>{{ error.message }}</p>
    </li>
  </ul>
</template>

<script>
export default {
  props: {
    errors: {
      type: Array[Error],
      required: true,
    },
  },
};
</script>
