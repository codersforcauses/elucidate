<template>
  <div class="drop-shadow-md bg-white w-[208px]">
    <div class="border h-[400px] rounded-t-[4px]">
      <p class="font-Montserrat font-light text-xl text-center relative top-[14px] text-centre">Filter Tags</p>
      <div class="bg-zinc-200 relative rounded-[95px] w-[182px] h-[43px] top-[34px] left-[11px]">
        <img class="relative w-[20px] h-[20px] top-[13px] left-[7px]" src="/static/avatar.svg" />
        <input v-model="searchedTag" placeholder="Search tags..." class="bg-transparent relative top-[-10px] left-[33px] w-[96px] h-[23px] outline-0 font-roboto"/>
      </div>
      <div class="relative top-[50px]">
        <SelectTag v-for="tag in searchedTags" :label="tag.name" :colour="tag.colour" @toggleTag="toggleTag($event)">
        </SelectTag>
      </div>
    <p>Selected Tags: {{ selectedTags }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SelectTag from "./SelectTag.vue"; // Do we need a form for the input?

export default {
  data() {
    return {
      searchedTag: "",
      // These tags should be generated using the getTags function at the start
      tags: [{ name: "math", colour: "bg-[#44a36b]", selected: false }, { name: "science", colour: "bg-[#5c2ad7]", selected: false }, { name: "history", colour: "bg-[#bd52a4]", selected: false }, { name: "geography", colour: "bg-[#aca127]" , selected: false }],
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
      const result = [];
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
      /* const axios = require("axios"); //Temporary axios call, but backend isn't hooked up yet
      const res = await axios.get(
        "/tags",
        { params: { searchedTag } }
      ) */ // Should be in form {name, colour, turned off}
    },

    toggleTag: function (name) {
      for (let tagIndex = 0; tagIndex < this.tags.length; tagIndex++) {
        if (this.tags[tagIndex].name === name) {
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