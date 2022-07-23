<template>
  <ValidationObserver class="w-11/12 max-w-lg">
    <form
      class="flex flex-col px-6 py-8 bg-green drop-shadow-lg"
      @submit.prevent="$emit('submit')"
    >
      <slot></slot>
    </form>
  </ValidationObserver>
</template>

<script>
import { ValidationObserver } from 'vee-validate';
export default {
  name: 'AuthForm',
  components: {
    ValidationObserver,
  },
};
</script>
