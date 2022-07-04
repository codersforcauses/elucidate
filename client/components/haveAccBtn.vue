<template>
  <!-- button that directs the user to the log in page -->
  <!-- button styling: ripple effect, inline-block (prevent the text inside from getting larger than the parent element, px py padding, mb margin, width full, 
  bg and text color + size,-->
  <a v-bind:href="logInPage"
  data-mdb-ripple="true" data-mdb-ripple-color="light" 
  class="inline-block text-center px-6 py-2.5 mt-6 mb-6 w-full 
  bg-indigo-500 text-white text-xl rounded shadow-md 
  hover:bg-indigo-600 hover:shadow-lg 
  focus:bg-indigo-600 focus:shadow-lg focus:outline-none focus:ring-0 
  active:bg-indigo-700 active:shadow-lg transition duration-300 ease-in-out">
    <div>I have an account</div>
  </a>
</template>

<script>
export default {
  name: 'haveAccBtn',
  data:function(){
    return{
      logInPage:'http://localhost:8080/login-page',
    };
  }
};
</script>