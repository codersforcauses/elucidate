<template>
  <div class="flex flex-inline">
    <div class="">
      <div class="">
        <!-- <img class="relative w-[20px] h-[20px] top-[13px] left-[7px]" src="../static/search.svg" /> -->
        <input
          v-model="searchedTerm"
          class="p-0 m-0 w-full h-9 rounded shadow-md"
          placeholder="Search tags..."
        />
      </div>
      <div class="flex">
        <SelectTag
          v-for="tag in searchedTags"
          :label="tag.name"
          :colour="tag.colour"
          @toggleTag="toggleTag($event)"
        >
        </SelectTag>
        <p class="pl-10 ml-0 text-white text-xl font-bold">
          Selected Tags: {{ selectedTags }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SelectTag from './SelectTag.vue'; // Do we need a form for the input?

export default {
  components: { SelectTag },
  data() {
    return {
      searchedTerm: '',
      // These tags should be generated using the getTags function at the start
      tags: [
        { name: 'math', colour: 'bg-[#44a36b]', selected: false },
        { name: 'science', colour: 'bg-[#5c2ad7]', selected: false },
        { name: 'history', colour: 'bg-[#bd52a4]', selected: false },
        { name: 'geography', colour: 'bg-[#aca127]', selected: false },
        { name: 'home economics', colour: 'bg-[#aca127]', selected: false },
      ],
    };
  },
  computed: {
    searchedTags() {
      const result = [];
      const search = this.searchedTerm.toLocaleLowerCase().trim();
      if (search === '') return result;
      this.tags.forEach((tag) => {
        if (tag.name.includes(search)) {
          result.push(tag);
        }
      });
      return result;
    },

    selectedTags: function () {
      const result = [];
      this.tags.forEach((tag) => {
        if (tag.selected) {
          result.push(tag.name);
        }
      });
      return result;
    },
  },
  methods: {
    getTags: function () {
      /* const axios = require("axios"); //Temporary axios call, but backend isn't hooked up yet
      const res = await axios.get(
        "/tags",
        { params: { searchedTag } }
      ) */
      // Should be in form {name, colour, turned off}
    },

    toggleTag: function (name) {
      for (let tagIndex = 0; tagIndex < this.tags.length; tagIndex++) {
        if (this.tags[tagIndex].name === name) {
          this.tags[tagIndex].selected = !this.tags[tagIndex].selected;
          break;
        }
      }
    },
  },
};
</script>

<style></style>
