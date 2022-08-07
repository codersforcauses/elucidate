<template>
  <div class="p-10 bg-white border border-gray-200 rounded-xl drop-shadow-md">
    <div>
      <nuxt-img src="Polygon.svg" class="float-left" />
      <div class="mx-11">
        <!-- Topic Name -->
        <div class="text-3xl font-bold font-openSans">
          {{ topicName }}
        </div>
        <!-- Subject Name -->
        <div class="text-xl my-1.5">{{ subjectName }}</div>

        <!-- Total questions and duration -->
        <div class="text-md font-roboto text-darkblue">
          <span class="mr-5">
            {{ totalQues }}
          </span>

          <span>
            <font-awesome-icon :icon="['fas', 'stopwatch']" />
            {{ totalHour }}
          </span>
        </div>
      </div>
      <!-- Start button component -->
      <StartButton />
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuizCard',
  data: function () {
    return {
      topicName: 'Topic Name',
      subjectName: 'Subject Name',
      totalQues: '50 questions',
      totalHour: '1hr',
    };
  },
};
</script>
