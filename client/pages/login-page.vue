<template>
  <div class="flex grow flex-col items-center content-center">
    <AuthHeader page-title="Sign In" />
    <AuthForm>
      <TextBox header="Email" input-type="text" />
      <TextBox
        header="Password"
        input-type="password"
        subtext="forgot password?"
        subtext-link="forgot-password"
      />
      <button
        class="place-self-center text-l font-bold text-red bg-white w-24 h-8 rounded border border-solid mb-7"
      >
        Login
      </button>
      <p class="place-self-center">
        don't have an account?
        <a
          href="sign-up"
          class="text-blue font-semibold underline underline-offset-2"
        >
          sign up!
        </a>
      </p>
    </AuthForm>
    <AuthFooter />
  </div>
</template>

<script>
import AuthFooter from '~/components/AuthFooter.vue';
import AuthHeader from '~/components/AuthHeader.vue';
import AuthForm from '~/components/Form/AuthForm.vue';
import TextBox from '~/components/Form/FormTextBox.vue';

export default {
  components: {
    AuthFooter,
    AuthHeader,
    AuthForm,
    TextBox,
  },
  layout: "auth",
};
</script>
