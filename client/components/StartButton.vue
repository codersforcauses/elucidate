<template>
  <div class="flex justify-center">
    <NuxtLink
      to="/quiz"
      data-mdb-ripple="true"
      data-mdb-ripple-color="light"
      class="inline-block w-2/5 px-6 py-1 mt-7 text-lg text-center text-white transition duration-300 ease-in-out bg-teal-300 shadow-md rounded-3xl hover:bg-teal-400 hover:shadow-lg focus:bg-teal-400 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-teal-500 active:shadow-lg"
      >Start</NuxtLink
    >
  </div>
</template>

<script>
export default {
  name: 'StartButton',
};
</script>
