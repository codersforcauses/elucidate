<template>
  <AuthForm
    v-if="!emailSentSuccess && !$route.query.uid"
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
    <div class="text-white" v-if="emailLoading">Sending email...</div>
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
    v-else-if="emailSentSuccess"
    class="gap-5 text-2xl font-bold text-white place-items-center"
  >
    <h1 class="text-3xl">Reset Link Has Been Sent!</h1>
    <font-awesome-icon
      :icon="['fas', 'fa-face-smile-beam']"
      class="text-[10rem] my-10"
    />
    <p class="text-center">
      Please check your spam folder if you cannot find the email.
    </p>
  </AuthForm>

  <AuthForm
    v-else-if="!passwordResetSuccess"
    v-slot="{ invalid }"
    error-header="Error resetting password, please fix the following errors:"
    :errors="errors"
    @submit="resetPassword"
  >
    <div class="mt-1 mb-3 text-white">
      <p v-if="uid !== ''" class="text-center">
        Resetting password for {{ uid }}
      </p>
      <p class="text-center">Please enter <wbr />a new password.</p>
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
    class="gap-5 text-2xl font-bold text-white place-items-center"
  >
    <h1 class="text-3xl text-center">Congratulations!</h1>
    <p class="text-center">
      Your password has been reset. Now you <wbr />can login with your new
      password!
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
    emailLoading: false,
    emailSentSuccess: false,
    uid: '',
    errors: [],

    emailField: {
      name: 'Email',
      type: 'email',
      index: 0,
      id: 'email',
      rules: 'required|email',
    },

    fields: [
      {
        name: 'Password',
        type: 'password',
        index: count++,
        id: 'password',
        rules: 'required|min:6',
      },
      {
        name: 'Confirm Password',
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

  async mounted() {
    this.resetPassword();
  },

  methods: {
    async sendResetLink(e) {
      this.emailLoading = true;
      const elements = e.target.elements;
      const data = {
        email: elements.Email.value,
      };

      const url = 'auth/reset/email/';
      await this.$axios
        .$post(url, data)
        .then((resp) => (this.emailSentSuccess = true))
        .catch((error) => {
          this.errors = error.response.data;
          this.emailLoading = false;
        });
    },

    async resetPassword(e = null) {
      const rawUid = this.$route.query.uid;
      const rawToken = this.$route.query.token;

      if (!rawUid) {
        return;
      }

      const formattedUid =
        rawUid.charAt(rawUid.length - 1) === '/'
          ? rawUid.substring(0, rawUid.length - 1)
          : rawUid;

      const formattedToken =
        rawToken.charAt(rawToken.lengthrawToken - 1) === '/'
          ? rawToken.substring(0, rawToken.length - 1)
          : rawToken;

      const url =
        'auth/reset/' + `?token=${formattedToken}&uid=${formattedUid}/`;

      try {
        this.uid = atob(formattedUid);
      } catch (err) {
        this.errors = { Errors: ['email UID is invalid'] };
        return;
      }

      if (e !== null) {
        const elements = e.target.elements;
        const data = {
          password: elements.Password.value,
        };
        await this.$axios
          .$put(url, data)
          .then((resp) => (this.passwordResetSuccess = true))
          .catch((error) => {
            this.errors = error.response.data;
            console.log(error.response.data);
          });
      } else {
        await this.$axios.$get(url).catch((error) => {
          this.errors = error.response.data;
          console.log(error.response.data);
        });
      }
    },
  },
};
</script>
