<template>
  <div class="flex flex-col mb-7">
    <h2 class="font-semibold mb-0.5">{{ header }}</h2>
    <input :type="inputType" class="drop-shadow-md h-11 w-full px-2" />
    <p v-if="subtext !== null && subtextLink === null">
      {{ subtext }}
    </p>
    <a
      v-else-if="subtextLink !== null"
      :href="subtextLink"
      class="place-self-end text-xs text-white font-semibold underline underline-offset-2 pt-1"
    >
      {{ subtext }}
    </a>
    <button type="button" v-if="inputType === 'password'" v-on:click="clickCheck" class="text-center h-10 px-1 mx-1 bg-white border-2 border-green2 rounded">
      SHOW
    </button>

  </div>
</template>

<script>
export default {
  name: 'TextBox',
  props: {
    header: String,
    subtext: {
      type: [String, null],
      optional: true,
      default: null,
    },
    subtextLink: {
      type: [String, null],
      optional: true,
      default: null,
    },
    inputType: {
      type: String,
      default: 'text',
      validator: function (value) {
        return ['text', 'password'].includes(value);
      },
    },
  },
  methods: {
    clickCheck: function() {
      this.inputType = "text";
      console.log(this.inputValue)
    }
  }
};
</script>
