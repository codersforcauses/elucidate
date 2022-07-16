<template>
  <div class="w-20 h-20 rounded-full bg-teal-200 flex justify-center shadow-md">
    <div
      class="w-16 h-16 rounded-full border-4 border-white mt-2 static"
    >
    <div class="w-16 h-16 absolute top-0 left-0">
      <svg class="text-center">
        <circle 
        stroke-width="4"
        stroke-linecap="round"
        :stroke-dasharray="circleDashArray"
        stroke="red"
        fill="transparent"
        r="30"
        cx="40"
        cy="40" />
      </svg>
      <span class="absolute top-7 left-5">{{ timeLeftFormatted }}</span>
    </div>

    </div>
    </div>
</template>

<script>
export default {
  name: 'CountdownTimer',
  data: function () {
    return {
      // Set the time limit in minute
      timeLimit: 4,
      timePassed: 0,
      timeInterval: null,
      // The number of dashes it needs to make a full circle stroke
      FullDashArray: 190
    };
  },
  methods: {
    // Set the interval to increment time passed by 1 every 60000 ms or 1 minute 
    startTimer() {
      this.timeInterval = setInterval(() => (this.timePassed += 1), 60000);
    },

    // Clear the interval 
    stopTimer() {
      clearInterval(this.timeInterval);
    },
  },
  computed: {
    timeLeft() {
      return this.timeLimit - this.timePassed;
    },

    // Specify the display of time left
    timeLeftFormatted() {
      // hours and minutes of the time left
      let hours = Math.floor(this.timeLeft / 60);
      let mins = this.timeLeft % 60;

      // Format the mins and hours to display 0 at the front when the time left is only 1 digit
      if (mins < 10) {
        mins = `0${mins}`;
      }
      if(hours < 10){
        hours = `0${hours}`;
      }
      return `${hours}:${mins}`;
    },

    // Divides the time left by the time limit to determine the portion of time left
    timeFraction(){
      return this.timeLeft / this.timeLimit;
    },

    // Update the dash array value by multiplying the time fraction with the full dash value, starting with 190
    circleDashArray(){
      return `${(this.timeFraction * this.FullDashArray).toFixed(0)} 190`;
    }
  },
  
  // Start the timer as window loads
  mounted: function () {
    this.startTimer();
  },

  watch: {
    // stop the timer (clear interval) when the timer reaches 0
    timeLeft(value) {
      if (value === 0) {
        this.stopTimer();
      }
    },
  },
};
</script>
