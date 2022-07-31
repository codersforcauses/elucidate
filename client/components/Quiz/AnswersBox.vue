<template>
  <div class="flex flex-inline">
    <label class="text-white mt-3 mr-5 text-l font-bold">{{ header }}</label>
    <input class="p-4 m-0 w-[700px] h-2 rounded shadow-md" :type="inputType">
  </div>
</template>

<script>
export default {
  name: 'AnswersBox',
  props: {
    header: String,
    inputType: String,
  },
};
</script>
