<template>
  <div class="pt-10 mb-5 ml-20">
    <div class="flex flex-inline">
      <label class="ml-14 pr-8 text-white text-xl font-bold">{{
        header
      }}</label>
      <FilterTags></FilterTags>
    </div>
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
