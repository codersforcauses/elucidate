<template>
  <ValidationObserver
    v-if="!accountCreated"
    v-slot="{ invalid }"
    slim
  >
    <div
      v-if="Object.keys(errors).length !== 0"
      class="mx-6 mt-8 bg-red w-11/12 p-3 text-neutral-100 font-bold rounded-md"
    >
      <font-awesome-icon :icon="['fas', 'circle-exclamation']" />
      <p class="inline">
        Error creating account, please fix the following errors:
      </p>
      <div
        v-for="(messages, error) in errors"
        :key="error"
        class="mt-2 text-lg"
      >
        {{ error }}
        <p v-for="(message, i) in messages" :key="i" class="text-base">
          {{ message }}
        </p>
      </div>
    </div>
    <AuthForm @submit.prevent="register">
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
  </ValidationObserver>
  <AuthForm v-else>
    <div
      class="flex flex-col grow items-center text-center font-bold text-white"
    >
      <p class="text-3xl my-5">Congratulations {{ name }}!</p>
      <p class="text-2xl mx-10 my-5">
        Your new Elucidate account has been created
      </p>
      <font-awesome-icon
        :icon="['fas', 'fa-face-smile-beam']"
        class="text-[10rem] my-10 text-white"
      />
      <p class="text-2xl mx-10 my-5">
        Please proceed to the
        <NuxtLink to="/quiz" class="text-blue">Home Page</NuxtLink> or
        <NuxtLink to="/login" class="text-blue">Search</NuxtLink>
        for quizzes
      </p>
    </div>
  </AuthForm>
</template>

<script>
import { ValidationObserver } from 'vee-validate';

let count = 0;
export default {
  name: 'SignupPage',
  auth: false,
  components: {
    ValidationObserver,
  },
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
          this.errors = error.response.data;
        });
    },
  },
};
</script>
