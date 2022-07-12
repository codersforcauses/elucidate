<template>
  <div class="w-20 h-20 rounded-full bg-teal-200 flex justify-center shadow-md">
    <div
      class="w-16 h-16 rounded-full border border-4 border-white mt-2 static"
    >
      <div
        class="w-16 h-16 rounded-full border border-4 border-red-400 absolute top-2 left-2"
      >
        <div class="text-center mt-4">{{ timeLeftFormatted }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CountdownTimer',
  data: function () {
    return {
      timeLimit: 3600,
      timePassed: 0,
      timeInterval: null,
    };
  },
  methods: {
    startTimer() {
      this.timeInterval = setInterval(() => (this.timePassed += 1), 1000);
    },
    stopTimer() {
      clearInterval(this.timeInterval);
    },
  },
  computed: {
    timeLeftFormatted() {
      const timeLeft = this.timeLimit - this.timePassed;
      const mins = Math.floor(timeLeft / 60);
      let seconds = timeLeft % 60;
      if (seconds < 10) {
        seconds = `0${seconds}`;
      }
      return `${mins}:${seconds}`;
    },
    timeLeft() {
      return this.timeLimit - this.timePassed;
    },
  },
  mounted: function () {
    this.startTimer();
  },
  watch: {
    timeLeft(value) {
      if (value === 0) {
        this.stopTimer();
      }
    },
  },
};
</script>
