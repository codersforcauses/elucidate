<template>
  <ValidationObserver
    v-slot="v"
    tag="form"
    class="flex flex-col px-6 py-8 bg-green drop-shadow-lg w-1/2 max-w-lg"
    @submit.prevent="(e) => $emit('submit', e)"
  >
    <slot :invalid="v.invalid" />
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
