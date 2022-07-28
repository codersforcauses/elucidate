<template>
  <AuthForm v-slot="{ invalid }" @submit="signin">
    <AuthAlert :errors="errors">
      Error while signing in, please fix the following errors:
    </AuthAlert>
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
        Sign up!
      </NuxtLink>
    </p>
  </AuthForm>
</template>

<script>
export default {
  layout: 'Auth',
  data() {
    return {
      errors: {},
    };
  },
  head: {
    title: 'Login',
  },
  methods: {
    async signin(e) {
      // Get the values from the form
      const elements = e.target.elements;
      const data = {
        email: elements.Email.value,
        password: elements.Password.value,
      };

      try {
        await this.$auth.loginWith('local', { data });
      } catch (error) {
        this.errors[error.name] = [error.message];
      }
    },
  },
};
</script>
