<template>
  <div class="w-1/2 max-w-lg">
    <AuthAlert v-if="errors.length !== 0" :errors="errors">
      {{ errorHeader }}
    </AuthAlert>
    <ValidationObserver
      v-slot="v"
      tag="form"
      class="flex flex-col px-6 py-8 bg-green drop-shadow-lg"
      @submit.prevent="(e) => $emit('submit', e)"
    >
      <slot :invalid="v.invalid" />
    </ValidationObserver>
  </div>
</template>

<script>
import { ValidationObserver } from 'vee-validate';
export default {
  name: 'AuthForm',
  components: {
    ValidationObserver,
  },
  props: {
    errors: {
      type: Array[Error],
      default: () => [],
    },
    errorHeader: {
      type: String,
      default: undefined,
    },
  },
};
</script>
