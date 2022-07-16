<template>
  <div class="flex flex-col">
      <Box title="Create a Quiz" :is-centered="true">
      <TextBox header='Quiz Name:'/>
      <p class="inline-flex font-thin px-1 text-xs text-white">(You can edit these later)</p><button class="inline-flex rounded-full shadow-sm bg-red text-white font-bold px-7 py-1">Next</button>
      </Box>
  </div>
</template>

<script>
import Box from '~/components/Box.vue';
import TextBox from '~/components/TextBox.vue';

export default {
  components: {
    Box,
    TextBox,
  },
};
</script>
