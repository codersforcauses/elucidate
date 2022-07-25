<template>
  <form
    class="flex flex-col px-6 py-8 bg-green drop-shadow-lg w-11/12 max-w-lg"
    @submit.prevent="$emit('submit')"
  >
    <slot />
  </form>
</template>

<script>
export default {
  name: 'AuthForm',
};
</script>
