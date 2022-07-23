<template>
  <div>
    <label>{{ header }}</label>
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
  props:{
    SelectTag: String,
    header: String,
    tag: Array,
  },
};
</script>
