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
        @buttonClicked="$emit('SelectAttri', label)"
        type="tertiary"
      >
        {{ buttonLabel }}
      </ButtonElement>
    </div>
  </div>
</template>

<script>
import ButtonElement from '../Input/ButtonElement.vue';
import ColouredBox from '../Quiz/ColouredBox.vue';
export default {
  components: { ButtonElement, ColouredBox },
  name: 'UserAttributeCard',
  data: () => ({
    commonColoredBoxStyles:
      'rounded-md text-white text-4xl font-extrabold h-20 w-20 flex justify-center items-center',
  }),
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
};
</script>
