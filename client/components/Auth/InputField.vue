<template>
  <div>
    <label class="font-semibold">{{ fieldName }}</label>
    <ValidationProvider :vid="id" :rules="rules" v-slot="{ errors, touched }">
      <div class="relative flex items-center -mt-2">
        <input
          v-if="fieldType != 'dropdown'"
          v-model="inputValue"
          :name="fieldName"
          :type="showText ? 'text' : fieldType"
          class="w-full h-10 px-2 my-3 drop-shadow-lg"
        />
        <div
          v-if="fieldType == 'password'"
          @mouseenter="toggleShowText"
          @mouseleave="toggleShowText"
          class="absolute right-0 top-auto bottom-auto left-auto w-10"
        >
          <font-awesome-icon
            :icon="['fas', 'fa-eye']"
            class="w-6 mx-2"
            :class="showText ? 'text-blue2' : 'text-gray-400'"
          />
        </div>
        <select
          v-if="fieldType == 'dropdown'"
          :name="fieldName"
          v-model="inputValue"
          class="w-full h-10 px-5 my-3 drop-shadow-lg"
        >
          <option selected disabled value="">Please Choose Grade...</option>
          <option
            v-for="(option, index) in fieldOptions"
            :key="index"
            :value="option"
            v-text="option"
          />
        </select>
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
    fieldName: {
      type: String,
      default: 'Field',
    },
    fieldType: {
      type: String,
      default: 'text',
    },
    isPassword: Boolean,
    fieldOptions: {
      type: Array,
      default: undefined,
    },
    id: {
      type: String,
      default: undefined,
    },
    rules: {
      type: String,
      default: undefined,
    },
  },
  data: () => ({
    showText: false,
    inputValue: '',
  }),
  methods: {
    toggleShowText: function () {
      this.showText = !this.showText;
    },
  },
};
</script>
