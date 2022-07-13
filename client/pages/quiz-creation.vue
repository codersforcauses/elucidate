<template>
  <Box title="Create a Quiz" :is-centered="true">
    <TextBox header="Quiz Name:" input-type="text"/>
    <!--<TextBox header="Tags" inputType="text"/> -->
    <TimeBox header="Time Limit:" input-type="text"/>
  </Box>
</template>

<script>
import Box from '~/components/Box.vue';
import TextBox from '~/components/TextBox.vue';
import TimeBox from '~/components/TimeBox.vue';

export default {
  components: {
    Box,
    TextBox,
    TimeBox,
  },
};
</script>
