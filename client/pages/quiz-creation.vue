<template>
  <Box title="Create a Quiz" :isCentered="true">
  </Box>
</template>

<script>
import Box from '~/components/Box.vue';
import TextBox from '~/components/TextBox.vue';
import TimeBox from '~/components/Timebox.vue';

export default {
  components: {
    Box,
    TextBox,
    TimeBox,
  },
};
</script>