<template>
  <div class="flex flex-inline mb-5 mx-10">
    <label class="flex align-text-top ml-5 pr-10 text-white text-xl font-bold">{{
      header
    }}</label>
    <textarea class="p-0 m-0 w-[520px] h-[100px] rounded shadow-md" :type="inputType"></textarea>
  </div>
</template>

<script>
export default {
  name: 'QuestionBox',
  props: {
    header: String,
    inputType: String,
  },
};
</script>
