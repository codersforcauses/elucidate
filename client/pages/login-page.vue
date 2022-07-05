<template>
  <div class="flex grow flex-col items-center content-center">
    <AuthHeader />

    <h1 class="italic text-3xl my-4 mr-7 flex gap-x-3 whitespace-nowrap">
      <img class="w-8" src="~/assets/avatar.svg" alt="Sign In Logo"  />
      Sign In
    </h1>

    <AuthForm>
      <TextBox header="Email" inputType="text" />
      <TextBox
        header="Password"
        inputType="password"
        subtext="forgot password?"
        subtextLink="forgot-password"
      />
      <button
        class="place-self-center text-l font-bold text-red bg-white w-24 h-8 rounded border border-solid mb-7"
      >
        Login
      </button>
      <p>
        don't have an account?
        <a href="sign-up" class="text-blue underline underline-offset-2">
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
import AuthForm from '~/components/form/AuthForm.vue';
import TextBox from '~/components/form/FormTextBox.vue';

export default {
  components: {
    AuthFooter,
    AuthHeader,
    AuthForm,
    TextBox,
  },
};
</script>
