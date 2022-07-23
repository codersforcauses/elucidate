<template>
  <div class="pt-10 mb-5 ml-20">
    <label class="p-10 pr-8 ml-0 text-white text-xl font-bold">{{
      header
    }}</label>
    <FilterTags></FilterTags>
    <SelectTag></SelectTag>
  </div>
</template>

<script>
import FilterTags from './FilterTags.vue';
import SelectTag from './SelectTag.vue';

export default {
  name: 'TagBox',
  components: {
    FilterTags,
    SelectTag,
  },
  props: {
    SelectTag: String,
    header: String,
    tag: Array,
  },
};
</script>
