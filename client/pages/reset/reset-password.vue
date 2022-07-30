<template>
  <div class="flex flex-col min-h-screen font-bold">
    <AuthHeader :page-title="'Reset Password'" />

    <div class="flex justify-center flex-grow">
      <AuthForm class="px-2">
        <div class="mt-1 mb-3">
          <p class="text-center text-white">
            Please enter a new<br />password for your login.
          </p>
        </div>
        <ValidationObserver v-slot="{ handleSubmit }">
          <form
            class="flex flex-col w-3/4 mx-6 my-5"
            @submit.prevent="handleSubmit(onSubmit)"
          >
            <InputField
              v-for="field in fields"
              :id="field.id"
              :key="field.index"
              class="w-80"
              :field-name="field.name"
              :field-type="field.type"
              :rules="field.rules"
              :is-password="field.isPassword"
            />
            <ButtonElement class="pt-4 pl-20"> Reset Password </ButtonElement>
          </form>
        </ValidationObserver>
      </AuthForm>
    </div>
    <AuthFooter />
  </div>
</template>

<script>
import { ValidationObserver } from 'vee-validate';
import ButtonElement from '@/components/Input/ButtonElement.vue';
import AuthForm from '@/components/Form/AuthForm.vue';
import InputField from '@/components/Form/InputField.vue';

let count = 0;
export default {
  name: 'SignupPage',
  components: { ButtonElement, ValidationObserver, AuthForm, InputField },
  data: () => ({
    fields: [
      {
        name: 'password',
        type: 'password',
        index: count++,
        id: 'password',
        rules: 'required|min:6',
        isPassword: true,
      },
      {
        name: 'confirm password',
        type: 'password',
        index: count++,
        id: 'confirm',
        rules: 'required|confirmed:password',
        isPassword: true,
      },
    ],
  }),

  methods: {
    onSubmit() {
      alert('submitted');
    },
  },
};
</script>
