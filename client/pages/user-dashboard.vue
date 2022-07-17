<template>
  <main>
    w
    <div class="flex items-center h-screen">
      <div class="p-9 flex-none w-1/3 h-full bg-blue4">
        <!-- background image, along with alignment of elements -->
        <div
          class="bg-[url('~/static/temp_Shapebg.svg')] bg-green4 justify-center bg-contain bg-no-repeat bg-center h-full w-full"
        >
          <!-- to be Profile pic -->
          <nuxt-img
            src="branding/logo_full.png"
            class="h-12"
            alt="Elucidate Logo Full"
          />

          <!-- to be Welcome text -->
          <div class="text-center content-around font-bold text-xl">
            Welcome {{ Temp_testPerson.name }}
          </div>

          <!-- to be your Email -->
          <div class="text-center font-thin">{{ Temp_testPerson.email }}</div>

          <!-- to be Edit Profile Button-->
          <div class="text-center">edit profile button</div>
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
