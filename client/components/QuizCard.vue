<template>
  <div class="p-5 bg-white rounded-xl border border-gray-200 drop-shadow-md">
    <div class="flex justify-left">
      <!-- Quiz tags - looping through an array of tags -->
      <div v-for="tag in tags" :key="tag.tagLabel" class="flex justify-end">
        <div class="text-center p-1 mr-2 mb-4
        bg-yellow-300 rounded-md">{{tag.tagLabel}}
        </div>
      </div>
    </div>
    <div>
      <img v-bind:src="arrowImage" class="float-left">
      <div class="ml-11">
        <!-- Topic Name -->
        <div class="text-black text-3xl">{{topicName}}</div>
        <!-- Subject Name -->
        <div class="text-black text-xl my-1.5">{{subjectName}}</div>
        <!-- Total questions and duration -->
        <div class="grid grid-cols-2">
          <div class="text-black text-md justify-self-start">{{totalQues}}</div>
          <div class="text-black text-md jusitfy-self-end">{{totalHour}}</div>
        </div>
      </div>
      <!-- Start button component -->
      <StartButton />
    </div>
  </div>
</template>


<script>
export default {
  name:'QuizCard',
  data:function(){
    return{
      arrowImage:require("~/assets/Polygon.svg"),
      topicName:'Topic Name',
      subjectName:'Subject Name',
      totalQues:'50 questions',
      totalHour:'1hr',
      tags:[
        {tagLabel: 'Tag 1'},
        {tagLabel: 'Tag 2'}
      ]
    };
  }
};
</script>
