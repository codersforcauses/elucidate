<template>
  <AuthForm>
    <form class="contents" @submit.prevent="login">
      <InputField class="w-full" field-name="Email" field-type="text" />
      <InputField class="w-full" field-name="Password" field-type="password" />
      <a
        href="/forgot-password"
        class="self-end text-xs font-semibold text-white underline underline-offset-2"
      >
        forgot password?
      </a>
      <button
        type="submit"
        class="place-self-center text-l font-bold text-red bg-white w-24 h-8 rounded border border-solid border-red my-5"
      >
        Login
      </button>
      <p class="place-self-center">
        don't have an account?
        <NuxtLink
          to="/signup"
          class="text-blue font-semibold underline underline-offset-2"
        >
          sign up!
        </NuxtLink>
      </p>
    </form>
  </AuthForm>
</template>

<script>
import AuthForm from '~/components/Auth/AuthForm.vue';
import InputField from '~/components/Auth/InputField.vue';

export default {
  components: {
    AuthForm,
    InputField,
  },

  layout: 'auth',
  data() {
    return {
      loginData: {
        username: '',
        password: '',
      },
    };
  },

  methods: {
    async login(e) {
      try {
        const response = await this.$auth.loginWith('local', {
          data: this.loginData,
        });
        console.log(response);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>
