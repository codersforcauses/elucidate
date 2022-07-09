<template>
  <div class="p-5 bg-white rounded-xl border border-gray-200 drop-shadow-md">
    <div class="flex justify-left">
      <div v-for="tag in tags" :key="tag.tagLabel" class="flex justify-end">
        <div class="text-center p-1 mr-2 mb-4
        bg-yellow-300 rounded-md">{{tag.tagLabel}}
        </div>
      </div>
    </div>
    <div>
      <img v-bind:src="arrowImage" class="float-left">
      <div class="ml-11">
        <div class="text-black text-3xl">{{topicName}}</div>
        <div class="text-black text-xl my-1.5">{{subjectName}}</div>
        <div class="grid grid-cols-2">
          <div class="text-black text-md justify-self-start">{{totalQues}}</div>
          <div class="text-black text-md jusitfy-self-end">{{totalHour}}</div>
        </div>
      </div>
      <StartButton />
    </div>
  </div>
</template>


<script>
import StartButton from '~/components/StartButton.vue';
export default {
  name:'QuizCard',
  components:{
    StartButton,
  },
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
