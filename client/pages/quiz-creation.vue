<template>
  <div class="flex flex-col">
      <Box title="Create a Quiz" :is-centered="true">
      <TextBox header='Quiz Name:'/>
      <TimeBox header='Time Limit:'/>

      <ObjectivesBox header='Objectives:'/>

      <div class="flex justify-end pb-2 pr-2">
        <p class="inline-flex self-center font-semibold px-1 text-xs text-white">(You can edit these later)</p>
        <button class="inline-flex rounded-full shadow-sm bg-red text-white font-bold px-7 py-1">Next</button>
      </div>
      </Box>
  </div>
</template>

<script>
import Box from '~/components/Box.vue';
import TextBox from '~/components/TextBox.vue';
import TimeBox from '~/components/TimeBox.vue';
import ObjectivesBox from '~/components/ObjectivesBox.vue';

export default {
  components: {
    Box,
    TextBox,
    TimeBox,
    ObjectivesBox,
  },
};
</script>
