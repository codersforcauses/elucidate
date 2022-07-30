<template>
  <div
    class="flex items-center h-10 bg-gray-200 rounded-md focus-within:outline focus-within:outline-2 focus-within:outline-gray-400"
  >
    <font-awesome-icon
      :icon="['fas', 'magnifying-glass']"
      class="mx-4 text-gray-400"
    />
    <input
      type="text"
      placeholder="Find a quiz"
      class="bg-transparent focus:outline-none"
    />
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
};
</script>
