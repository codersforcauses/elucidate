<template>
<div>
  <img
  id="logo" 
  src="~/assets/elucidate-logo.jpg"
  alt="Elucidate Logo">
    
   
<div class="sign-in">
  <h1><em>Sign in</em></h1>
</div>


<div class="enter-info" id="box"> 
    <h2>Email</h2>
    <input type="text">

    <h2>Password</h2>
    <input type="password">
    <a href="forgot-password" id="password"><u>forgot password?</u></a>

    <button id="login">Login</button>

    <p>don't have an account? <a href="sign-up" id="sign-up"><u>sign up!</u></a></p>
</div>
</div>  
</template>

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
