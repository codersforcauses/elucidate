<template>
  <main>
    <div class="flex h-screen">
      <div class="p-9 flex-none w-1/3 h-full">
        <!-- background image, along with alignment of elements -->
        <div
          class="flex flex-col justify-center items-center content-evenly space-y-3 h-full bg-[url('~/static/temp_Shapebg.svg')] bg-contain bg-no-repeat bg-center"
        >
          <!-- to be Profile pic -->
          <nuxt-img
            src="branding/logo.svg"
            class="h-52"
            :alt="User.name + ' profile picture'"
          />

          <!-- to be Welcome text -->
          <div class="font-bold text-xl">
            Welcome {{ User.name }}
          </div>

          <!-- to be your Email -->
          <div class="font-thin">{{ User.email }}</div>

          <ButtonElement to="/edit-Profile" type="primary" class=""
            >Edit Profile</ButtonElement
          >
        </div>
      </div>

      <div class="flex-1 flex-row h-full"></div>
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
      profPicUrl: '',
    },
    
  }),
  beforeMount() {
    this.User = this.getUserData();
    console.log(this.User)
  }, 
  methods: {
    getUserData() {
      return this.Temp_testPerson;
    }
  },   
};
</script>
