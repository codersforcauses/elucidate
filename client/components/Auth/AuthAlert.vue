<template>
  <div
    v-if="Object.keys(errors).length !== 0"
    class="bg-red p-3 m-6 text-neutral-100 font-bold rounded-md"
  >
    <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
    <p class="inline">
      <slot> Please fix the following errors: </slot>
    </p>
    <div v-for="(messages, error) in errors" :key="error" class="mt-2 text-lg">
      {{ error }}
      <p v-for="(message, i) in messages" :key="i" class="text-base">
        {{ message }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    errors: {
      type: Array,
      required: true,
    },
  },
};
</script>
