<template>
  <main>
    <div class="flex items-center h-screen">
      <div class="p-9 bg-green4 flex-none w-1/3 h-full">

        <!-- background image, along with alignment of elements -->
        <div
          class="bg-[url('~/static/temp_Shapebg.svg')] justify-center content-center bg-contain bg-no-repeat bg-center h-full w-full"
        >
          <!-- to be Profile pic -->
          <div class=""></div>

          <!-- to be Welcome text -->
          <div class="text-center font-bold text-xl">Welcome {{ Temp_testPerson.name }}</div>

          <!-- to be your Email -->
          <div class="text-center font-thin">{{ Temp_testPerson.email }}</div>

          <!-- to be Edit Profile Button-->
          <div class="text-center">edit profile</div>
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
