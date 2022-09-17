<template>
  <AuthForm
    v-if="!$route.query.token"
    v-slot="{ invalid }"
    error-header="Error sending reset link, please fix the following errors:"
    :errors="errors"
    @submit="sendResetLink"
  >
    <div class="mt-1 mb-3">
      <p class="text-center text-white">
        Please enter <wbr />your registered email.
      </p>
    </div>
    <InputField
      :id="emailField.id"
      :key="emailField.index"
      :field-name="emailField.name"
      :field-type="emailField.type"
      :field-options="emailField.options"
      :rules="emailField.rules"
      :inputvalue.sync="emailField.value"
    />
    <AuthSubmit :disabled="invalid">Send Reset Link</AuthSubmit>
  </AuthForm>

  <AuthForm
    v-else-if="!passwordResetSuccess"
    v-slot="{ invalid }"
    error-header="Error resetting password, please fix the following errors:"
    :errors="errors"
    @submit="resetPassword"
  >
    <div class="mt-1 mb-3">
      <p class="text-center text-white">Please enter <wbr />a new password.</p>
    </div>
    <InputField
      v-for="field in fields"
      :id="field.id"
      :key="field.index"
      :field-name="field.name"
      :field-type="field.type"
      :field-options="field.options"
      :rules="field.rules"
      :inputvalue.sync="field.value"
    />
    <AuthSubmit :disabled="invalid">Reset Password</AuthSubmit>
  </AuthForm>

  <AuthForm
    v-else
    class="place-items-center gap-5 font-bold text-2xl text-white"
  >
    <h1 class="text-3xl">Congratulations!</h1>
    <p>
      Your password has been reset. Now you <wbr />can login with your new
      password
    </p>
    <font-awesome-icon
      :icon="['fas', 'fa-face-smile-beam']"
      class="text-[10rem] my-10"
    />
    <p>
      Please proceed to the
      <NuxtLink to="/login" class="text-blue">login page</NuxtLink> to login!
    </p>
  </AuthForm>
</template>

<script>
let count = 0;

export default {
  name: 'ResetPassword',
  auth: false,
  layout: 'auth',

  data: () => ({
    title: 'Reset Password',
    passwordResetSuccess: false,
    errors: [],

    emailField: {
      name: 'email',
      type: 'email',
      index: 0,
      id: 'email',
      rules: 'required|email',
    },

    fields: [
      {
        name: 'password',
        type: 'password',
        index: count++,
        id: 'password',
        rules: 'required|min:6',
      },
      {
        name: 'confirm password',
        type: 'password',
        index: count++,
        id: 'confirm',
        rules: 'required|password:@password',
      },
    ],
  }),
  head() {
    return {
      title: this.title,
    };
  },
  methods: {
    onSubmit() {
      alert('submitted');
    },

    sendResetLink() {},
    resetPassword() {},
  },
};
</script>
