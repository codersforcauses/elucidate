<template>
  <main>
    <div class="flex h-screen">
      <!-- left hand side -- should be component ? -->
      <div class="p-9 flex-none w-1/3 h-full">
        <LeftBanner
          :email="Temp_testPerson.email"
          :name="User.name"
          :profilePic="User.profilePic"
        />
      </div>

      <!-- right hand side - should be component?-->
      <div class="flex-1 flex-row h-full">
        <!-- right hand side, top  -->
        <div class="space-y-6">
          <h1 class="font-bold text-xl">Overview</h1>
          <div class="flex flex-row space-x-6">
            <UserAttributeCard property="Quizzes Answered"/>
            <UserAttributeCard property="Quizzes Created"/>
            <UserAttributeCard property="User Attribute"/>
          </div>
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
import UserAttributeCard from '../components/Dashboard/UserAttributeCard.vue';

export default {
  name: 'UserDashboard',
  components: { LeftBanner, UserAttributeCard },
  data: () => ({
    User: {},

    Temp_testPerson: {
      name: 'Lorem Ipsum',
      email: 'LoremIpsum@gmail.com',
      profilePic: 'tempProfPic.png',
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
