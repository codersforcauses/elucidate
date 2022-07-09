<template>
  <div>
    <label>{{ fieldName }}</label>

    <ValidationProvider :vid="id" :rules="rules" v-slot="{ errors }">
      <div class="relative flex items-center">
        <input
          v-if="isPassword && !showText"
          :name="fieldName"
          type="password"
          class="w-full h-10 drop-shadow-lg my-3 px-2"
          v-model="inputValue"
        />
        <input
          v-else
          :name="fieldName"
          :type="fieldType"
          class="w-full h-10 drop-shadow-lg my-3 px-2"
          v-model="inputValue"
        />
        <font-awesome-icon
          :icon="['fas', 'fa-eye']"
          class="w-6 text-grey-400"
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
    inputValue: ""
  }),
  props: {
    fieldName: String,
    fieldType: String,
    isPassword: Boolean,
    id: String,
    rules: String,
  },
  methods: {
    clickCheck: function () {
      this.showText = !this.showText;
    },
  },
};
</script>
