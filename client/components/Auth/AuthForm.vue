<template>
  <form
    class="flex flex-col px-6 py-8 bg-green drop-shadow-lg"
  >
    <slot />
  </form>
</template>

<script>
export default {
  name: 'AuthForm',
};
</script>
