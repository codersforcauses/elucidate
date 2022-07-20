<template>
  <main>
    <div class="flex h-screen ">
      <!-- left hand side -- should be component ? -->
      <div class="p-7 px- w-[28rem] flex-none h-full">
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
              label="Quizzes Finished"
              buttonLabel="View Finished Quizzes"
              :value="User.stats.quizzesAnswered"
              color="green"
              @SelectAttri="(label) => selectedAttri = label"
            />
            <UserAttributeCard
              label="Quizzes Created"
              buttonLabel="View Your Quizzes"
              :value="User.stats.quizzesMade"
              color="yellow"
              @SelectAttri="(label) => selectedAttri = label"
            />
            <UserAttributeCard
              label="User Attribute"
              buttonLabel="View Your Attributes"
              :value="User.stats.userAttribute"
              color="red"
              @SelectAttri="(label) => selectedAttri = label"
            />
          </div>
        </div>
        <!-- right hand side, bottom part -->
        <div v-if="selectedAttri === 'Quizzes Finished'" class="h-1/2">
          <h1 class="font-black text-2xl">Finished Quizzes</h1>
          <QuizList :quizzes="Temp_quizzesAnswered"/> 
        </div>
        <div v-if="selectedAttri === 'Quizzes Created'" class="h-1/2">
          <h1 class="font-black text-2xl">Your Quizzes</h1>
          <QuizList :quizzes="Temp_quizzesMade"/> 
        </div>
        <div v-if="selectedAttri === 'User Attribute'" class="h-1/2">
          <h1 class="font-black text-2xl">Your Attributes</h1>
            <UserAttributeCard
              label="User Attribute"
              buttonLabel="View Your Attributes"
              :value="User.stats.userAttribute"
              color="red"
              @SelectAttri="(label) => selectedAttri = label"
            />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import LeftBanner from '../components/Dashboard/LeftBanner.vue';
import QuizList from '../components/Quiz/QuizList.vue';
import UserAttributeCard from '../components/Dashboard/UserAttributeCard.vue';

export default {
  name: 'UserDashboard',
  components: { LeftBanner, UserAttributeCard, QuizList},
  data: () => ({
    User: { stats: {},},
    quizzesAnswered: [],
    quizzesMade: [],
    selectedAttri: "Quizzes Finished",

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
      name: 'Maths - Integrals II',
      tags: [{name: 'Calculus', color: 'red'}, {name: 'Year 12', color: 'yellow'}],
      author: 'NicholasJDavies',
      dateCreated: Date.now(),
      score: 57,
     }, 
     {
      name: 'Maths - Integrals I',
      tags: [{name: 'Calculus', color: 'blue'}, {name: 'Year 11', color: 'yellow'}],
      author: 'JohnnyBoi42',
      dateCreated: Date.now(),
      score: 57,
     }, 
     {
      name: 'Chemistry - Organic',
      tags: [{name: 'Chemistry', color: 'red'}, {name: 'Organic', color: 'blue'}],
      author: 'Ms. Vujcich',
      dateCreated: Date.now(),
      score: 80,
     }, 
     {
      name: 'Which Avengers are you?',
      tags: [{name: 'Silly', color: 'green'}, {name: 'notAThing', color: 'yellow'}],
      author: 'BuzzFeed',
      dateCreated: Date.now(),
      score: "Iron Man",
     }, 
    ],
    Temp_quizzesMade: [
     {
      name: 'Star Signs',
      tags: [{name: 'Astrology', color: 'red'}, {name: 'Beliefs', color: 'yellow'}],
      author: 'Lorem Ipsum',
      dateCreated: Date.now(),
     }, 
     {
      name: 'Latin - 1',
      tags: [{name: 'Language', color: 'blue'}, {name: 'Latin', color: 'yellow'}],
      author: 'Lorem Ipsum',
      dateCreated: Date.now(),
      score: 99,
     }, 
     {
      name: 'What is the shape of Italy?',
      tags: [{name: 'Geography', color: 'red'}, {name: 'World', color: 'blue'}],
      author: 'Lorem Ipsum',
      dateCreated: Date.now(),
     },
    ],
  }),
  beforeMount() {
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
