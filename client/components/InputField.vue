<template>
  <div>
    <label>{{ fieldName }}</label>
    <input type="fieldType" class="w-full h-10 drop-shadow-lg mt-2 mb-4" />
  </div>
</template>

<script>
export default {
  name: 'InputField',
  props: {
    fieldName: String,
    fieldType: String,
  },
};
</script>
