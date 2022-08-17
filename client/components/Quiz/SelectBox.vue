<template>
  <div class="flex items-center mr-5 w-auto" @click="select">
    <div
      class="rounded-full px-3 text-black hover:shadow-lg transition-shadow duration-200 ease-in-out"
      :class="isSelected ? 'bg-aquablue font-semibold' : 'bg-aquablue2'"
    >
      <p class="select-none m-2 whitespace-nowrap">{{ label }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SelectBox',
  props: {
    label: {
      type: String,
      default: '',
    },
  },
  data: () => ({
    isSelected: false,
  }),
  methods: {
    select: function () {
      this.isSelected = !this.isSelected;
      this.$emit('getData', this.isSelected);
    },
  },
};
</script>
