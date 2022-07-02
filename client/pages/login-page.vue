<template>
<div>
    
    <div class="flex flex-grow flex-col items-center content-center">
        <AuthHeader/>
        <h1 class="italic text-3xl my-4">Sign In</h1>

        <div class="flex flex-col bg-green/75 py-6 px-10 rounded drop-shadow-lg mb-10">
            <h2 class="font-bold mb-0.5">Email</h2><input type="text" class="drop-shadow h-10 w-full">

            <h2 class="font-bold mb-0.5 mt-2">Password</h2><input type="password" class="drop-shadow h-10 w-full">
            <a href="forgot-password" class="place-self-end text-xs text-white underline underline-offset-2 pb-10 pt-1">forgot password?</a>

            <button class="place-self-center text-xl font-bold text-red bg-white w-20 h-auto rounded border border-solid mb-7">Login</button>
            <p>don't have an account? <a href="sign-up" class="text-blue underline underline-offset-2">sign up!</a></p>
            </div>
        </div>
        <AuthFooter/>
    </div>
</template>

<script>
import AuthFooter from '~/components/AuthFooter.vue'
import AuthHeader from '~/components/AuthHeader.vue'

export default {
    components: {
        AuthFooter,
        AuthHeader
    },
}
</script>

<!--
<style>

div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: 'Montserrat';

}

#logo {
    height: 50px;
    width: auto;
    margin: 15px;
}

.sign-in {
    font-size: 150%;
    margin: 0 0 15px 0;
}

#box {
    background-color: #53DFCB73;
    height: 200px;
    width: 200px;
    padding: 10px;
}

h2 {
    text-align: left;
    font-size: 80%;
    font-weight: bold;

}

#password {
    font-size: 20%;
    color: white;
    margin: 0 0 5px 0;
    text-align: right;
}

#login {
    background-color: white;
    color: #F54A87;
    border: 1px solid #F54A87;
    border-radius: 3px;
    font-size: 80%;
    font-weight: bold;
    padding: 1px 10px 1px 10px;
    margin: 0 0 10px 0;
}

p,
#sign-up {
    display: flex;
    flex-direction: row;
    font-size: 50%;
    justify-content: space-evenly;
}

p {
    margin: 0 0 0 5px;
}

#sign-up{
    color: #7087FF;
}

</style>

-->
