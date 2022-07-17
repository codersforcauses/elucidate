<template>
  <div class="flex flex-col min-h-screen">
    <AuthHeader :page-title="title" />

    <div class="flex justify-center flex-grow">
      <AuthForm v-if="!accountCreated">
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
            <!-- <button v-else type="submit" :disabled="invalid" class="w-24 h-8 mt-5 font-bold bg-white border border-solid rounded place-self-center text-l text-red">Submit</button> -->
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
        Congratulations! Your account has been created.
        <NuxtLink to="/quiz" class="text-blue"> Click here </NuxtLink>
        to go to the home page, or
        <NuxtLink to="/login" class="text-blue"> Click here </NuxtLink>
        to begin searching for quizes.
      </AuthForm>
      <!-- Add sign up form here? -->
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
    ispassword: true,
    btnDisable: true,
    accountCreated: false,
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
    onSubmit() {
      alert('Form has been submitted!');
      this.accountCreated = true;
    },
    async register(e) {
      const postData = {};
      this.fields.forEach((field) => {
        postData[field.id] = e.target.elements[field.name].value;
      });

      await this.$axios
        .post('auth/register/', postData)
        .then((data) => console.log(data))
        .catch((error) => {
          console.log(error.response.data);
          // TODO: Display error messages on duplicate email and form errors
          this.$router.push('signup-error');
        });

      this.$router.push('login');
    },
  },
};
</script>
