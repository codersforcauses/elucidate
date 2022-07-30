<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader :page-title="title" />

    <div class="flex justify-center flex-grow">
      <AuthForm v-if="!accountCreated">
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

        <ValidationObserver v-slot="{ invalid }" class="w-full">
          <form
            class="flex flex-col w-11/12 mx-6 my-8"
            @submit.prevent="register"
          >
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
            <button
              type="submit"
              :disabled="invalid"
              :class="
                invalid ? 'text-darkgrey bg-lightgrey' : 'text-red bg-white'
              "
              class="w-24 h-8 mt-5 font-bold border border-solid rounded place-self-center text-l drop-shadow-lg"
            >
              Submit
            </button>
          </form>
        </ValidationObserver>
        <p>
          Already have an account?
          <NuxtLink to="/login" class="text-blue"
            >Click here to log in</NuxtLink
          >
        </p>
      </AuthForm>

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
            <NuxtLink to="/quiz" class="text-blue">Login page</NuxtLink> to
            login!
          </p>
        </div>
      </AuthForm>
    </div>
    <AuthFooter />
  </div>
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
