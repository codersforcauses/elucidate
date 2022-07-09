<template>
  <div>
    <label>{{ fieldName }}</label>

    <ValidationProvider :vid="id" :rules="rules" v-slot="{ errors }">
      <div class="relative flex items-center">
        <input
          v-if="isPassword && !showText"
          :name="fieldName"
          type="password"
          class="w-full h-10 dropShadow my-3 px-2"
          :value="inputvalue"
          @input="$emit('update:inputvalue', $event.target.value)"
        />
        <input
          v-else
          :name="fieldName"
          :type="fieldType"
          class="w-full h-10 dropShadow my-3 px-2"
          :value="inputvalue"
          @input="$emit('update:inputvalue', $event.target.value)"
        />
        <img
          v-if="isPassword"
          @mouseover="clickCheck"
          @mouseleave="clickCheck"
          class="w-6 mx-2 absolute top-auto bottom-auto left-auto right-0"
          src="~/assets/eye.svg"
        />
      </div>
      <span class="text-red">{{ errors[0] }}</span>
    </ValidationProvider>
  </div>
</template>

<script>
// Validation
// ---------------------------------------
import { ValidationProvider, extend } from 'vee-validate';
import { required, email, min } from 'vee-validate/dist/rules';

extend('email', {
  ...email,
  message: 'Invalid email address',
});

extend('required', {
  ...required,
  message: 'This field is required',
});

extend('min', {
  ...min,
  message: '{_field_} must have at least {length} characters',
});

extend('password', {
  params: ['target'],
  validate(value, { target }) {
    return value === target;
  },
  message: 'Password confirmation does not match',
});
// ---------------------------------------

export default {
  name: 'InputField',
  components: {
    ValidationProvider,
  },
  data: () => ({
    showText: false,
    test: 'test',
  }),
  props: {
    fieldName: String,
    fieldType: String,
    isPassword: Boolean,
    id: String,
    rules: String,
    inputvalue: String,
  },
  methods: {
    clickCheck: function () {
      this.showText = !this.showText;
    },
  },
};
</script>
