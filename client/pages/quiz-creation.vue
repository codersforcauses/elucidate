<template>
  <Box title="Create a Quiz" :isCentered="true">
    <TextBox header="Quiz Name:" inputType="text"/>
    <!--<TextBox header="Tags" inputType="text"/> -->
    <TimeBox header="Time Limit:" inputType="text"/>
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