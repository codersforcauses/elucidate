<template>
  <div
    class="h-[15.5rem] w-[15.75rem] hover:shadow-lg transition-shadow duration-200 ease-in-out"
  >
    <div
      class="flex flex-col space-y-2 justify-center items-center bg-lightgrey/75 h-full"
    >
      <ColouredBox :color="color" :value="value" />

      <div>
        <p class="text-lg font-medium">
          {{ label }}
        </p>
      </div>
      <ButtonElement
        type="tertiary"
        @buttonClicked="$emit('SelectAttri', label)"
      >
        {{ buttonLabel }}
      </ButtonElement>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserAttributeCard',
  props: {
    label: {
      type: String,
      default: undefined,
    },
    buttonLabel: {
      type: String,
      default: undefined,
    },
    value: {
      type: Number,
      default: 0,
    },
    color: {
      type: String,
      default: 'green',
    },
  },
  data: () => ({
    commonColoredBoxStyles:
      'rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center',
  }),
};
</script>
