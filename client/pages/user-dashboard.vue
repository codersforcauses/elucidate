<template>
  <main>
    <div class="flex h-screen">
      <div class="p-9 flex-none w-1/3 h-full bg-blue4">
        <!-- background image, along with alignment of elements -->
        <div
          class="flex flex-col justify-center items-center content-evenly h-full bg-[url('~/static/temp_Shapebg.svg')] bg-contain bg-no-repeat bg-center bg-green4"
        >
          <!-- to be Profile pic -->
          <nuxt-img
            src="branding/logo.svg"
            class="h-52"
            :alt="Temp_testPerson.name + ' profile picture'"
          />

          <!-- to be Welcome text -->
          <div class="font-bold text-xl">
            Welcome {{ Temp_testPerson.name }}
          </div>

          <!-- to be your Email -->
          <div class="font-thin">{{ Temp_testPerson.email }}</div>

          <!-- to be Edit Profile Button-->
          <div class="">edit profile button</div>
        </div>
      </div>

      <div class="bg-yellow4 flex-1 flex-row h-full"></div>
    </div>
  </main>
</template>

<script>
export default {
  name: 'UserDashboard',

  data: () => ({
    Temp_testPerson: {
      name: 'Lorem Ipsum',
      email: 'LoremIpsum@gmail.com',
      profPicUrl: '',
    },
  }),
};
</script>
