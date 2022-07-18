<template>
  <main>
    <div class="flex h-screen">
      <!-- left hand side -- should be component ? -->
      <div class="p-9 flex-none w-1/3 h-full">
        <LeftBanner />
      </div>

      <!-- right hand side - should be component?-->
      <div class="flex-1 flex-row h-full">
        <!-- right hand side, top  -->
        <div class="">
          <h1 class="font-bold text-xl">Overview</h1>
        </div>
        <!-- right hand side, bottom part -->
        <div class="">
          <h1 class="font-bold text-xl">Your Quizzes</h1>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import LeftBanner from '../components/Dashboard/LeftBanner.vue';
export default {
  components: { LeftBanner },
  name: 'UserDashboard',

  data: () => ({
    User: {},

    Temp_testPerson: {
      name: 'Lorem Ipsum',
      email: 'LoremIpsum@gmail.com',
      profPic: 'tempProfPic.png',
    },
  }),
  beforeMount() {
    this.User = this.getUserData();
  },
  methods: {
    getUserData() {
      return this.Temp_testPerson;
    },
  },
};
</script>
