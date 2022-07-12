<template>
    <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
    <div class="bg-blue-600 h-2.5 rounded-full" :style="{width: `${(this.curr_question / this.max_questions) * 100}%`}"></div>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        curr_question: 33,
        max_questions: 50
      }
    },
    methods: {
      completeQuestion() {
        this.value = Math.random() * this.max
      },
      clicked() {
        this.curr_question = this.completeQuestion
      }
    },
    props:[
        'curr_question',
        'max_questions',
    ]
  }
</script>