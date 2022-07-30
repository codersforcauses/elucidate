<template>
  <div class="flex flex-inline">
    <label
      class="flex align-text-top w-[175px] p-10 pr-0 ml-10 text-white text-xl font-bold"
      >{{ header }}</label
    >
    <textarea
      class="p-0 ml-0 w-[520px] h-15 rounded shadow-md"
      :type="inputType"
    ></textarea>
    <!-- <textarea id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500" placeholder="Your message..."></textarea>  --->
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
