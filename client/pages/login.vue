<template>
  <AuthForm
    v-slot="{ invalid }"
    error-header="Error while signing in, please fix the following errors:"
    :errors="errors"
    @submit="signin"
  >
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
        to="/sign-up"
        class="text-blue font-semibold underline underline-offset-2"
      >
        Sign up!
      </NuxtLink>
    </p>
  </AuthForm>
</template>

<script>
export default {
  layout: 'auth',
  data() {
    return {
      errors: [],
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

      await this.$auth
        .login({ data })
        .then((resp) => this.$auth.setUserToken(resp.data))
        .catch((error) => (this.errors = error.response.data));
    },
  },
};
</script>
