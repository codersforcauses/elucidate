<template>
  <div class="flex flex-col min-h-screen font-bold">
    <AuthHeader :page-title="'Reset Password'" />
    <div class="flex justify-center flex-grow">
      <AuthForm class="px-2">
        <font-awesome-layers class="mx-3 fa-3x">
          <font-awesome-icon
            size="lg"
            class="text-center text-white"
            icon="fa-regular fa-circle"
          />
          <font-awesome-icon
            size="xs"
            class="pl-3 text-center text-white"
            icon="fa-solid fa-envelope"
          />
        </font-awesome-layers>

        <div class="mt-4 mb-3">
          <p class="text-center text-white">
            Please enter your email to reset your password
          </p>
        </div>
        <ValidationObserver v-slot="{ handleSubmit }">
          <form
            class="flex flex-col w-3/4 mx-6 my-5"
            @submit.prevent="handleSubmit(onSubmit)"
          >
            <InputField
              class="w-80"
              :field-name="field.name"
              :field-type="field.type"
              :rules="field.rules"
            />
            <ButtonElement class="pt-4 pl-20"> Get Reset Link </ButtonElement>
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

export default {
  name: 'SignupPage',
  components: { ButtonElement, ValidationObserver, AuthForm, InputField },
  data: () => ({
    field: {
      name: 'Email',
      type: 'email',
      id: 'email',
      rules: 'required|email',
    },
  }),
  methods: {
    onSubmit() {
      alert('submitted');
    },
  },
};
</script>
