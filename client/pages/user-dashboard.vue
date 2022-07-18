<template>
  <main>
    <div class="flex h-screen">

      <!-- left hand side -- should be component ? -->
      <div class="p-9 flex-none w-1/3 h-full">
        <!-- background image, along with alignment of elements -->
        <div
          class="flex flex-col justify-center items-center content-evenly space-y-3 h-full bg-[url('~/static/temp_Shapebg.svg')] bg-contain bg-no-repeat bg-center"
        >
          <!-- to be Profile pic -->
          <nuxt-img
            :src="User.profPic ? User.profPic : '/avatar.svg'"
            class="h-52"
            :alt="User.name + ' profile picture'"
          />

          <!-- to be Welcome text -->
          <div>
            <p class="font-bold text-xl">
              Welcome {{ User.name }}
            </p>
          </div>

          <!-- to be your Email -->
          <div class="font-thin">{{ User.email }}</div>

          <ButtonElement to="/edit-Profile" type="primary" class=""
            >Edit Profile</ButtonElement
          >
        </div>
      </div>

      <!-- right hand side - should be component?-->
      <div class="bg-green4 flex-1 flex-row h-full">
        <!-- right hand side, top  -->
        <div class="">
          <h1 class="font-bold text-xl" > 
            Overview
          </h1>
        </div>
        <!-- right hand side, bottom part -->
        <div class="">
          <h1 class="font-bold text-xl"> 
            Your Quizzes
          </h1>

        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
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
    }
  },   
};
</script>
