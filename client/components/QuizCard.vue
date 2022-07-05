<template>
  <div class="p-5 bg-white rounded-xl border border-gray-200 drop-shadow-md">
    <div class="flex justify-left">
      <span v-for="tag in tags" :key="tag.tagLabel">
        <span class="inline-block text-center p-1 mr-2 mb-4
        bg-yellow-300 rounded-md">{{tag.tagLabel}}
        </span>
      </span>
    </div>
    <div>
      <img v-bind:src="arrowImage" class="float-left">
      <div>
        <div class="text-black text-3xl ml-10">{{topicName}}</div>
        <div class="text-black text-xl ml-11 my-1.5">{{subjectName}}</div>
        <span class="text-black text-md ml-11">{{totalQues}}</span>
        <span class="text-black text-md ml-5">{{totalHour}}</span><br />
        <StartButton />
      </div>
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
