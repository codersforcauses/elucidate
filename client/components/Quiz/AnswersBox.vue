<template>
  <div class='flex flex-inline'>
    <label class="flex ml-[60px] mr-[30px] pr-10 text-white text-xl font-bold">{{ header }}</label>
    <input
      class="p-4 m-[6px] mr-0 w-[520px] h-7 rounded shadow-md"
      :type="inputType"
    />
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
