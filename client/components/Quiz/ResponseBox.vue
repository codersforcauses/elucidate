<template>
  <div class="flex flex-inline">
    <textarea
      class="p-0 ml-[13px] w-[700px] h-[100px] rounded shadow-md"
      :type="inputType"
    ></textarea>
  </div>
</template>

<script>
export default {
  name: 'AnswersBox',
  props: {
    inputType: String,
  },
};
</script>
