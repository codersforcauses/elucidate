<template>
  <div>
    <label>{{ fieldName }}</label>
    <ValidationProvider :vid="id" :rules="rules" v-slot="{ errors, touched }">
      <div class="relative flex items-center">
        <input
          :name="fieldName"
          :type="showText ? 'text' : fieldType"
          class="w-full h-10 px-2 my-3 drop-shadow-lg"
          v-model="inputValue"
        />
        <div
          v-if="fieldType == 'password'"
          @mouseenter="clickCheck"
          @mouseleave="clickCheck"
          class="w-10 absolute top-auto left-auto bottom-auto right-0"
        >
          <font-awesome-icon
            :icon="['fas', 'fa-eye']"
            class="w-6 mx-2"
            :class="showText ? 'text-blue2' : 'text-gray-400'"
          />
        </div>
      </div>
      <span v-if="touched" class="text-red">{{ errors[0] }}</span>
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
  data: function () {
    return {
      showText: false,
      inputValue: '',
    };
  },
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
