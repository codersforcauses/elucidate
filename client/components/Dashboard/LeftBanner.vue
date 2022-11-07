<template>
  <!-- background image, along with alignment of elements -->
  <div
    class="flex flex-col justify-center items-center content-evenly space-y-2 h-full bg-[url('~/static/temp_Shapebg.svg')] bg-contain bg-no-repeat bg-center"
  >
    <!--Profile pic -->
    <nuxt-img
      :src="profilePic"
      class="h-52 mb-3"
      :alt="name + ' profile picture'"
    />

    <!--Welcome text -->
    <div>
      <p class="font-extrabold text-xl mb-1">Welcome {{ name }}.</p>
    </div>

    <!--Email-->
    <p class="font-thin text-sm">{{ email }}</p>

    <ButtonElement to="/edit-Profile" type="tertiary" class=""
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
