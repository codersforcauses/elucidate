<template>
    <div class="flex flex-grow flex-col items-center content-center">
        <AuthHeader />
            <div>
                <div class="flex place-content-center bg-green">
                    <h1 class="text-center text-3xl font-bold">Create a quiz</h1>
                </div>
                <AuthForm>
                    <TextBox header="Quiz Name" inputType="text" />
                    <TextBox header="Tags" inputType="text"/>
                    <TextBox header="Time Limit" inputType="number"/>
                </AuthForm>
            </div>
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