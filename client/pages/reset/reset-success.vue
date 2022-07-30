<template>
  <div class="flex flex-col min-h-screen font-bold">
    <AuthHeader :page-title="'Password Reset!!'" />
    <div class="flex justify-center flex-grow">
      <AuthForm class="w-1/2 h-2/5">
        <font-awesome-icon size="4x" icon="fa-regular fa-face-smile" />

        <div class="mt-4 mb-3">
          <p class="text-xl font-black text-center text-white">
            Congrats! Your password has been reset. Now you <br />can login with
            your new password
          </p>
        </div>
        <ButtonElement to="login-page" class="py-3">
          Return to login
        </ButtonElement>
      </AuthForm>
    </div>
    <AuthFooter />
  </div>
</template>

<script>
import ButtonElement from '@/components/Input/ButtonElement.vue';
import AuthForm from '@/components/Form/AuthForm.vue';

export default {
  name: 'SignupPage',
  components: { ButtonElement, AuthForm },
  data: () => ({}),
};
</script>
