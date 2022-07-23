<template>
  <div>
    <label class="p-10 text-black text-md font-bold">{{ header }}</label>
    <input class="p-2 ml-[80px] mr-0 w-1/2 h-7 rounded shadow-md" :type="inputType" />
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
