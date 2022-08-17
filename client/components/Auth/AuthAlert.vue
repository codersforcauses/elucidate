<template>
  <ul class="bg-red p-3 my-6 text-neutral-100 font-bold rounded-md list-disc">
    <h1>
      <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
      <slot> Please fix the following errors: </slot>
    </h1>
    <li
      v-for="(messages, error) in errors"
      :key="error.toString()"
      class="ml-8 mt-2"
    >
      <h2 class="">
        {{ (error.charAt(0).toUpperCase() + error.slice(1)).replace(/_/, ' ') }}
      </h2>
      <p
        v-for="message in messages"
        :key="message.toString()"
        class="ml-8 font-normal"
      >
        {{ message }}
      </p>

      <p></p>
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
