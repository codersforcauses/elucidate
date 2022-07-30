<template>
  <div class="flex flex-inline mb-5">
    <textarea
      class="p-0 mx-5 w-[700px] h-[100px] rounded shadow-md"
      :type="inputType"
    ></textarea>
  </div>
</template>

<script>
export default {
  name: 'QuestionBox',
  props: {
    inputType: String,
  },
};
</script>
