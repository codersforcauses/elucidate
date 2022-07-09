<template>
  <div class="flex flex-col mb-7">
    <h2 data-test="formTextBoxLabel" class="font-semibold mb-0.5">
      {{ header }}
    </h2>
    <input :type="inputType" class="drop-shadow-md h-11 w-full px-2" />
    <p
      v-if="subtext !== null && subtextLink === null"
      data-test="formTextBoxSubText"
    >
      {{ subtext }}
    </p>
    <a
      v-else-if="subtextLink !== null"
      data-test="formTextBoxSubText"
      :href="subtextLink"
      class="place-self-end text-xs text-white font-semibold underline underline-offset-2 pt-1"
    >
      {{ subtext }}
    </a>
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
};
</script>
