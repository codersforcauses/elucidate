<template>
  <div class="flex flex-col z-10">
    <Box title="Create a Quiz" :is-centered="true">
      <TextBox header="Quiz Name:" />
      <TagBox header="Tags: " />
      <TimeBox header="Time Limit:" />

      <ObjectivesBox header="Objectives:" />

      <div class="flex justify-end pb-2 pr-2">
        <p
          class="inline-flex self-center font-semibold px-1 text-xs text-white"
        >
          (You can edit these later)
        </p>
        <QuizButton>Next</QuizButton>
      </div>
    </Box>
  </div>
</template>

<script>
import Box from '~/components/Box.vue';
import TextBox from '~/components/TextBox.vue';
import TimeBox from '~/components/TimeBox.vue';
import ObjectivesBox from '~/components/ObjectivesBox.vue';
import QuizButton from '~/components/Quiz/QuizButton.vue';
import image from '~/assets/ambient_shapes.png';
import TagBox from '~/components/TagBox.vue';

export default {
  components: {
    Box,
    TextBox,
    TimeBox,
    ObjectivesBox,
    QuizButton,
    TagBox,
  },
  data: () => ({
    bgImage: image,
  }),
};
</script>
