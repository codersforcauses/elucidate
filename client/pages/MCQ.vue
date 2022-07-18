<template>
    <div>
        <!--The time allocated to the quiz bubble:-->
        <label class="bg-blue2 px-10 py-2 text-white font-semibold text-md rounded shadow-sm"><FontAwesomeIcon :icon="['fa', 'stopwatch']" />1hr</label>

        <h1 class="text-4xl mt-7">Create A Quiz</h1>

        <div class="flex flex-col">
            <Box title="{Display Quiz Name}" :is-centered="false">

            <div class="flex inline-flex mt-10 mb-5 mx-20">
                <p class="flex align-middle mr-8 text-white text-l font-bold">Question Type:</p>
                <div class="flex inline-flex gap-2  text-white text-md font-bold">
                    <button class="bg-yellow rounded-full shadow-sm shadow-sm px-3 py-1">Multiple Choice</button>
                    <button class="bg-blue rounded-full shadow-sm px-3 py-1">Short Answer</button>
                    <button class="bg-red rounded-full shadow-sm px-3 py-1">Numeric Question</button>
                </div>
            </div>
            <QuestionBox header="Question:"></QuestionBox>

            <div class="flex flex-col columns-4 gap-2 ml-10">
                <AnswersBox header="Question A:"></AnswersBox>
                <AnswersBox header="Question B:"></AnswersBox>
                <AnswersBox header="Question C:"></AnswersBox>
                <AnswersBox header="Question D:"></AnswersBox>
            </div>
            
            <div class="flex place-content-end m-5">
            <QuizButton color="red" class="mr-10">+ Add Question</QuizButton>
            <QuizButton color="red">Finish</QuizButton>
            </div>
            </Box>
        </div>
    </div>
</template>

<script>
import Box from '~/components/Box.vue';
import QuestionBox from '~/components/QuestionBox.vue';
import AnswersBox from '~/components/AnswersBox.vue';
import QuizButton from '~/components/Quiz/QuizButton.vue';

export default {
components: {
    Box,
    QuestionBox,
    AnswersBox,
    QuizButton,
}}
</script>
