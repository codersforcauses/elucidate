<template>
  <ValidationObserver
    v-if="!accountCreated"
    v-slot="{ invalid }"
    class="w-11/12 max-w-lg"
  >
    <AuthForm @submit="onSubmit()">
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
import AuthForm from '~/components/Auth/AuthForm.vue';
import InputField from '~/components/Auth/InputField.vue';
import AuthSubmit from '~/components/Auth/AuthSubmit.vue';

let count = 0;
export default {
  name: 'SignupPage',
  components: {
    AuthForm,
    AuthSubmit,
    InputField,
    ValidationObserver,
  },
  layout: 'auth',
  data: () => ({
    title: 'Sign-Up',
    password: '',
    confirm: '',
    ispassword: true,
    btnDisable: true,
    accountCreated: false,
    name: '',
    fields: [
      {
        name: 'First Name',
        type: 'text',
        index: count++,
        id: 'firstname',
        rules: 'required',
      },
      {
        name: 'Last Name',
        type: 'text',
        index: count++,
        id: 'lastname',
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
    onSubmit() {
      this.title = 'Account Created!';
      this.name = document.getElementsByName('First Name')[0].value;
      this.accountCreated = true;
    },
  },
};
</script>
