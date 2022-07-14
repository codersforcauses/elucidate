<template>
  <div class="border drop-shadow-md fill-blue bg-white w-44">
    <p>Filter Tags</p>
    <input v-model="searchedTag" placeholder="Search tags..." class="bg-zinc-200 rounded-3xl" />
    <div>
      <SelectTag v-for="tag in searchedTags" :label="tag.name" :selected="tag.selected" @toggleTag="toggleTag($event)">
      </SelectTag>
    </div>
    <p>Selected Tags: {{ selectedTags }}</p>
  </div>
</template>

<script>
import axios from "axios";
import SelectTag from "./SelectTag.vue"; //Do we need a form for the input?

export default {
  data() {
    return {
      searchedTag: "",
      //These tags should be generated using the getTags function at the start
      tags: [{ name: "math", selected: false }, { name: "science", selected: false }, { name: "history", selected: false }, { name: "geography", selected: false }],
    };
  },
  components: { SelectTag },
  computed: {
    searchedTags: function () {
      this.result = [];
      this.tags.forEach(tag => {
        if (tag.name.includes(this.searchedTag)) {
          this.result.push(tag);
        }
      });
      return this.result;
    },

    selectedTags: function () {
      let result = [];
      this.tags.forEach(tag => {
        if (tag.selected) {
          result.push(tag.name);
        }
      });
      return result;
    }
  },
  methods: {
    getTags: function () {
      /*const axios = require("axios"); //Temporary axios call, but backend isn't hooked up yet
      const res = await axios.get(
        "/tags",
        { params: { searchedTag } }
      )*/ //Should be in form {name, colour, turned off}
    },

    toggleTag: function (name) {
      for (let tagIndex = 0; tagIndex < this.tags.length; tagIndex++) {
        if (this.tags[tagIndex].name == name) {
          this.tags[tagIndex].selected = !this.tags[tagIndex].selected;
          break;
        }
      }
    }
  }
}
</script>

<style>
</style>