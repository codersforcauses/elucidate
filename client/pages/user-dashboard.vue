<template>
  <main>
    <div class="flex h-screen">
      <!-- left hand side -- should be component ? -->
      <div class="p-9 flex-none w-1/3 h-full">
        <LeftBanner
          :email="Temp_testPerson.email"
          :name="User.first_name"
          :profilePic="User.profilePic"
        />
      </div>

      <!-- right hand side - should be component?-->
      <div class="flex flex-1 flex-col h-full">
        <!-- right hand side, top  -->
        <div class="h-1/2 px-4 py-9">
          <h1 class="font-extrabold text-xl mb-4">Overview</h1>
          <div class="flex flex-row space-x-6">
            <UserAttributeCard
              property="Quizzes Answered"
              :propertyValue="User.stats.quizzesAnswered"
              color="green"
            />
            <UserAttributeCard
              property="Quizzes Created"
              :propertyValue="User.stats.quizzesMade"
              color="yellow"
            />
            <UserAttributeCard
              property="User Attribute"
              :propertyValue="User.stats.userAttribute"
              color="red"
            />
          </div>
        </div>
        <!-- right hand side, bottom part -->
        <div class="h-1/2">
          <h1 class="font-black text-2xl">Quizzes Answered</h1>
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
    User: { stats: {},},

    Temp_testPerson: {
      first_name: 'Lorem',
      last_name: 'Ispum',
      email: 'LoremIpsum@gmail.com',
      profilePic: 'tempProfPic.png',
      stats: {
        quizzesAnswered: 42,
        quizzesMade: 17,
        userAttribute: 27,
      },
    },
    Temp_quizzesAnswered: [
     {
      Name: 'Maths - Integrals II',
      Tags: ['Calculus', 'Year 12'],
      Author: NicholasJDavies,
      DateCreated: Date.now(),
      Score: 57,
     }, 
     {
      Name: 'Maths - Integrals I',
      Tags: ['Calculus', 'Year 11'],
      Author: 'JohnnyBoi42',
      DateCreated: Date.now(),
      Score: 57,
     }, 
     {
      Name: 'Chemistry - Organic',
      Tags: ['Chemistry', 'Organic'],
      Author: 'Ms. Vujcich',
      DateCreated: Date.now(),
      Score: 80,
     }, 
     {
      Name: 'Which Avengers are you?',
      Tags: ['Silly', 'notAThing'],
      Author: 'BuzzFeed',
      DateCreated: Date.now(),
      Score: 100,
     }, 
    ],
    Temp_quizzesMade: [

    ],
  }),
  beforeMount() {
    console.log(this.Temp_testPerson.stats.userAttribute)
    this.User = this.getUserData();
    this.quizzesMade = this.getQuizzesMade();
    this.quizzesAnswered = this.getQuizzesAnswered();
  },
  methods: {
    getUserData() {
      return this.Temp_testPerson;
    },
    getQuizzesAnswered() {
      return this.Temp_quizzesAnswered;
    },
    getQuizzesMade() {
      return this.Temp_quizzesMade;
    },
  },
};
</script>
