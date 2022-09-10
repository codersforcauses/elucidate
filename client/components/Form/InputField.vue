<template>
  <div>
    <label class="font-semibold" :for="fieldName">{{ fieldName }}</label>
    <ValidationProvider
      v-slot="{ errors, touched }"
      slim
      :vid="id"
      :rules="rules"
    >
      <div class="relative flex items-center -mt-2">
        <input
          v-if="fieldType !== 'dropdown'"
          :id="fieldName"
          v-model="inputValue"
          :name="fieldName"
          :type="showText ? 'text' : fieldType"
          class="w-full h-10 px-2 my-3 drop-shadow-lg"
        />
        <div
          v-if="fieldType === 'password'"
          class="absolute right-0 top-auto bottom-auto left-auto w-10"
          @mouseenter="clickCheck"
          @mouseleave="clickCheck"
        >
          <font-awesome-icon
            :icon="['fas', 'fa-eye']"
            class="w-6 mx-2"
            :class="showText ? 'text-blue2' : 'text-gray-400'"
          />
        </div>
        <select
          v-if="fieldType === 'dropdown'"
          :id="fieldName"
          v-model="inputValue"
          :name="fieldName"
          class="w-full h-10 px-5 my-3 drop-shadow-lg"
        >
          <option selected disabled value="">
            Please Choose Your Grade...
          </option>
          <option
            v-for="(option, index) in fieldOptions"
            :id="fieldName"
            :key="index"
            :value="option"
            v-text="option"
          />
        </select>
      </div>
      <span class="text-red">{{ errors[0] }}</span>
    </ValidationProvider>
  </div>
</template>

<script>
// Validation
// ---------------------------------------
import { ValidationProvider, extend } from 'vee-validate';
import {
  required,
  email,
  min,
  digits,
  confirmed,
} from 'vee-validate/dist/rules';

extend('email', {
  ...email,
  message: 'Invalid email address',
});

extend('confirmed', {
  ...confirmed,
  message: "Passwords don't match",
});

extend('required', {
  ...required,
  message: 'This field is required',
});

extend('min', {
  ...min,
  message: '{_field_} must have at least {length} characters',
});

extend('digits', {
  ...digits,
  message: '{length} digits required',
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
  props: {
    fieldName: String,
    fieldType: String,
    isPassword: Boolean,
    id: String,
    rules: String,
  },
  data: () => ({
    showText: false,
    inputValue: '',
  }),
  watch: {
    inputValue: function (newInputValue) {
      this.$emit('input', newInputValue);
    },
  },
  methods: {
    clickCheck: function () {
      this.showText = !this.showText;
    },
  },
};
</script>
