<template>
  <AuthForm v-if="!accountCreated" v-slot="{ invalid }" @submit="register">
    <AuthAlert :errors="errors">
      Error creating account, please fix the following errors:
    </AuthAlert>
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
    <AuthSubmit :disabled="invalid">Submit</AuthSubmit>
    <p class="self-center mt-3">
      Already have an account?
      <NuxtLink to="/login" class="text-blue">Click here to log in</NuxtLink>
    </p>
  </AuthForm>
  <AuthForm v-else class="items-center text-center font-bold text-white">
    <p class="text-3xl my-5">Congratulations {{ name }}!</p>
    <p class="text-2xl my-5">
      Your new Elucidate account <br />
      has been created
    </p>
    <font-awesome-icon
      :icon="['fas', 'fa-face-smile-beam']"
      class="text-[10rem] my-10"
    />
    <p class="text-2xl mx-10 my-5">
      Please proceed to the
      <NuxtLink to="/quiz" class="text-blue">Home Page</NuxtLink> or
      <NuxtLink to="/login" class="text-blue">Search</NuxtLink>
      for quizzes
    </p>
  </AuthForm>
</template>

<script>
let count = 0;
export default {
  name: 'SignupPage',
  auth: false,
  layout: 'auth',
  data: () => ({
    title: 'Sign-Up',
    accountCreated: false,
    name: '',
    errors: {},
    fields: [
      {
        name: 'First Name',
        type: 'text',
        index: count++,
        id: 'first_name',
        rules: 'required',
      },
      {
        name: 'Last Name',
        type: 'text',
        index: count++,
        id: 'last_name',
        rules: 'required',
      },
      {
        name: 'Email',
        type: 'text',
        index: count++,
        id: 'email',
        rules: 'required|email',
      },
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
      {
        name: 'Grade',
        type: 'dropdown',
        options: ['Grade 11', 'Grade 12', 'Other'],
        index: count++,
        id: 'grade',
        rules: 'required',
      },
    ],
  }),
  head: {
    title: 'Sign Up',
  },
  methods: {
    async register(e) {
      const postData = {};
      this.fields.forEach((field) => {
        postData[field.id] = e.target.elements[field.name].value;
      });

      await this.$axios
        .post('auth/register/', postData)
        .then(() => {
          this.title = 'Account Created!';
          this.name = e.target.elements['First Name'].value;
          this.accountCreated = true;
        })
        .catch((error) => {
          if (error.response) {
            this.errors = error.response.data;
          } else if (error.request) {
            this.errors['No Response'] = [error.request];
          } else {
            this.errors['Unknown Error'] = [error.message];
          }
        });
    },
  },
};
</script>
