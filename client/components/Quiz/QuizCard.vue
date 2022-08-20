<template>
  <div class="p-10 bg-white border border-gray-200 rounded-xl drop-shadow-md">
    <div class="flex items-start">
      <nuxt-img src="Polygon.svg" />
      <div class="ml-6">
        <!-- Topic Name -->
        <div class="text-3xl font-bold font-openSans">
          {{ topicName }}
        </div>
        <!-- Subject Name -->
        <div class="text-xl my-1.5">{{ subjectName }}</div>

        <!-- Total questions and duration -->
        <div class="text-md font-roboto text-darkblue">
          <span class="mr-5 whitespace-nowrap">
            {{ totalQues }}
          </span>

          <span class="whitespace-nowrap">
            <font-awesome-icon :icon="['fas', 'stopwatch']" />
            {{ totalHour }}
          </span>
        </div>
      </div>
      <font-awesome-icon
        :icon="['fas', subjectIcon]"
        :class="`text-9xl flex-grow
            ${subjectColor}`"
      />
    </div>
    <!-- Start button component -->
    <StartButton />
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
      subjectIcon: 'calculator',
      subjectColor: 'text-red',
    };
  },
};
</script>
