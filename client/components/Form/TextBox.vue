<template>
  <div class="flex flex-col mb-7">
    <h2 class="font-semibold mb-0.5">{{ header }}</h2>
    <input :type="inputType" class="w-full px-2 drop-shadow-md h-11" />
    <p v-if="subtext !== null && subtextLink === null">
      {{ subtext }}
    </p>
    <a
      v-else-if="subtextLink !== null"
      data-test="formTextBoxSubText"
      :href="subtextLink"
      class="pt-1 text-xs font-semibold text-white underline place-self-end underline-offset-2"
    >
      {{ subtext }}
    </a>
    <button
      v-if="inputType === 'password'"
      type="button"
      class="h-10 px-1 mx-1 text-center bg-white border-2 rounded border-green2"
      @click="clickCheck"
    >
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
    clickCheck: function () {
      this.inputType = 'text';
      console.log(this.inputValue);
    },
  },
};
</script>
