<template>
  <main>
    <div class="flex items-center justify-between h-screen"> 
      <div class="pg-11  p-11 my-4 bg-green4 flex-none w-1/3 h-full"> 
        <div class="bg-[url('~/static/temp_Shapebg.svg')] bg-contain bg-no-repeat bg-center h-full w-full">

          <!-- to be Profile pic -->
          <div class=""> 

          </div>

          <!-- to be Welcome text -->
          <div class="">
            Welcome {{Temp_testPerson.name}}
          </div>

          <!-- to be your Email -->
          <div class="">
            sample {{Temp_testPerson.email}}
          </div>
          
          <!-- to be Edit Profile Button-->
          <div class="">
            edit profile
          </div>
        </div>
      </div>

      <div class="bg-yellow4 flex-1 flex-row h-full">

      </div>

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
