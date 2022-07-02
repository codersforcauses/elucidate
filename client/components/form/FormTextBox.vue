<template>
  <div class="flex flex-col mb-2">
    <h2 class="font-bold mb-0.5">{{ header }}</h2>
    <input :type="inputType" class="drop-shadow h-10 w-full" />
    <p v-if="subtext !== null && subtextLink === null">
      {{ subtext }}
    </p>
    <a
      v-else-if="subtextLink !== null"
      :href="subtextLink"
      class="place-self-end text-xs text-white underline underline-offset-2 pb-10 pt-1"
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
