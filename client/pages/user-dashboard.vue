<template>
  <main>
    <div class="flex h-screen">
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
              label="Quizzes Taken"
              buttonLabel="View Taken Quizzes"
              :value="User.stats.quizzesTaken"
              color="green"
              @SelectAttri="(label) => (selectedAttri = label)"
            />
            <UserAttributeCard
              label="Questions Created"
              buttonLabel="View Your Questions"
              :value="User.stats.quizzesMade"
              color="red"
              @SelectAttri="(label) => (selectedAttri = label)"
            />
          </div>
        </div>
        <!-- right hand side, bottom part -->
        <div v-if="selectedAttri === 'Quizzes Taken'" class="h-1/2">
          <h1 class="font-black text-2xl">Taken Quizzes</h1>
          <QuizList :quizzes="Temp_quizzesTaken" />
        </div>
        <div v-if="selectedAttri === 'Questions Created'" class="h-1/2">
          <h1 class="font-black text-2xl">Your Questions</h1>
          <QuizList :quizzes="Temp_quizzesMade" />
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
  components: { LeftBanner, UserAttributeCard, QuizList },
  data: () => ({
    User: { stats: {} },
    quizzesTaken: [],
    quizzesMade: [],
    selectedAttri: 'Quizzes Taken',

    Temp_testPerson: {
      first_name: 'Lorem',
      last_name: 'Ispum',
      email: 'LoremIpsum@gmail.com',
      profilePic: 'tempProfPic.png',
      stats: {
        quizzesTaken: 42,
        quizzesMade: 17,
        userAttribute: 27,
      },
    },
    Temp_quizzesTaken: [
      {
        name: 'Maths - Integrals II',
        tags: [
          { name: 'Calculus', color: 'red' },
          { name: 'Year 12', color: 'yellow' },
        ],
        dateCreated: Date.now(),
        score: 57,
      },
      {
        name: 'Maths - Integrals I',
        tags: [
          { name: 'Calculus', color: 'blue' },
          { name: 'Year 11', color: 'yellow' },
        ],
        dateCreated: Date.now(),
        score: 57,
      },
      {
        name: 'Chemistry - Organic',
        tags: [
          { name: 'Chemistry', color: 'red' },
          { name: 'Organic', color: 'blue' },
        ],
        dateCreated: Date.now(),
        score: 80,
      },
      {
        name: 'Which Avenger are you?',
        tags: [
          { name: 'Silly', color: 'green' },
          { name: 'notAThing', color: 'yellow' },
        ],
        dateCreated: Date.now(),
        score: 78,
      },
    ],
    Temp_quizzesMade: [
      {
        name: 'Star Signs',
        tags: [
          { name: 'Astrology', color: 'red' },
          { name: 'Beliefs', color: 'yellow' },
        ],
        dateCreated: Date.now(),
      },
      {
        name: 'Latin - 1',
        tags: [
          { name: 'Language', color: 'green' },
          { name: 'Latin', color: 'yellow' },
        ],
        dateCreated: Date.now(),
        score: 99,
      },
      {
        name: 'What is the shape of Italy?',
        tags: [
          { name: 'Geography', color: 'red' },
          { name: 'World', color: 'blue' },
        ],
        dateCreated: Date.now(),
      },
    ],
  }),
  beforeMount() {
    this.User = this.getUserData();
    this.quizzesMade = this.getQuizzesMade();
    this.quizzesTaken = this.getQuizzesTaken();
  },
  methods: {
    getUserData() {
      return this.Temp_testPerson;
    },
    getQuizzesTaken() {
      return this.Temp_quizzesTaken;
    },
    getQuizzesMade() {
      return this.Temp_quizzesMade;
    },
  },
};
</script>
