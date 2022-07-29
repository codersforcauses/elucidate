<template>
  <multiselect
    v-model="value"
    :options="options"
    :multiple="multiple"
    :close-on-select="closeOnSelect"
    :clear-on-select="clearOnSelect"
    :preserve-search="preserveSearch"
    :hide-selected="hideSelected"
    :placeholder="placeholder"
    class="rounded-lg beginQuizSelector"
  >
  </multiselect>
</template>

<script>
import Multiselect from 'vue-multiselect';

export default {
  name: 'QuizInput',
  components: {
    Multiselect,
  },
  props: {
    options: {
      type: Array,
      default: undefined,
    },
    multiple: {
      type: Boolean,
      default: false,
    },
    closeOnSelect: {
      type: Boolean,
      default: true,
    },
    clearOnSelect: {
      type: Boolean,
      default: false,
    },
    preserveSearch: {
      type: Boolean,
      default: false,
    },
    hideSelected: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
      default: '',
    },
  },
  data: () => ({
    value: [],
  }),
  methods: {
    getValue() {
      this.$emit('getData', this.value);
    },
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
.beginQuizSelector .multiselect__tag,
.beginQuizSelector .multiselect__option--highlight,
.beginQuizSelector .multiselect__option--highlight::after {
  background-color: #fcd47c;
  color: black;
}

.beginQuizSelector .multiselect__tag i:hover {
  background-color: #d19a24;
  color: black;
}

.beginQuizSelector .multiselect__tags {
  border-radius: 6px;
  font-size: 16px;
  border-width: 0px;
}
.beginQuizSelector .multiselect__placeholder {
  margin-bottom: 0px;
  padding-top: 0px;
}
</style>
