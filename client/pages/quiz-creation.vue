<template>
  <div class="flex flex-col">
      <Box title="Create a Quiz" :is-centered="true">
      <TextBox header='Quiz Name:'/>
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
