<template>
  <!-- background image, along with alignment of elements -->
  <div
    class="flex flex-col justify-center items-center content-evenly space-y-3 h-full bg-[url('~/static/temp_Shapebg.svg')] bg-contain bg-no-repeat bg-center"
  >
    <!--Profile pic -->
    <nuxt-img :src="profilePic" class="h-52" :alt="name + ' profile picture'" />

    <!--Welcome text -->
    <div>
      <p class="font-bold text-xl">Welcome {{ name }}</p>
    </div>

    <!--Email-->
    <p class="font-thin">{{ email }}</p>

    <ButtonElement to="/edit-Profile" type="primary" class=""
      >Edit Profile</ButtonElement
    >
  </div>
</template>

<script>
export default {
  name: 'LeftBanner',
  props: {
    name: {
      type: String,
      default: undefined,
    },
    email: {
      type: String,
      default: undefined,
    },
    profilePic: {
      type: String,
      default: '/avatar.svg',
    },
  },
};
</script>
