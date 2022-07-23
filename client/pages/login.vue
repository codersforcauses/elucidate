<template>
  <AuthForm v-slot="{ invalid }">
    <InputField
      id="email"
      class="w-full"
      rules="required|email"
      field-name="Email"
      field-type="text"
    />
    <InputField
      id="password"
      class="w-full"
      rules="required"
      field-name="Password"
      field-type="password"
    />
    <NuxtLink
      to="/forgot-password"
      class="self-end text-xs font-semibold text-white underline underline-offset-2"
    >
      forgot password?
    </NuxtLink>
    <AuthSubmit :disabled="invalid">Login</AuthSubmit>
    <p class="place-self-center">
      Don't have an account?
      <NuxtLink
        to="/signup"
        class="text-blue font-semibold underline underline-offset-2"
      >
        sign up!
      </NuxtLink>
    </p>
  </AuthForm>
</template>

<script>
import AuthForm from '~/components/Auth/AuthForm.vue';
import InputField from '~/components/Auth/InputField.vue';
import AuthSubmit from '~/components/Auth/AuthSubmit.vue';

export default {
  components: {
    AuthForm,
    AuthSubmit,
    InputField,
  },
  layout: 'auth',
  head: {
    title: 'Login',
  },
};
</script>
