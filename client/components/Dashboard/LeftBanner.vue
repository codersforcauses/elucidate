<template>
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
      <p class="font-bold text-xl">Welcome {{ User.name }}</p>
    </div>

    <!-- to be your Email -->
    <div class="font-thin">{{ User.email }}</div>

    <ButtonElement to="/edit-Profile" type="primary" class=""
      >Edit Profile</ButtonElement
    >
  </div>
</template>

<script>
export default {
  name: 'LeftBanner',
};
</script>
