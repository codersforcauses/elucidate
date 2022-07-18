<template>
    <div>
        <h1>Create A Quiz</h1>
        <div class="flex flex-col">
            <Box title="{Display Quiz Name}" :is-centered="false">

            <div class="flex inline-flex mt-10 mb-5 mx-20">
                <p class="flex align-bottom mr-8 text-white text-l font-bold">Question Type:</p>
                <div class="flex inline-flex gap-2  text-white text-md font-bold">
                    <button class="bg-yellow rounded-full shadow-sm shadow-sm px-3 py-1">Multiple Choice</button>
                    <button class="bg-blue rounded-full shadow-sm px-3 py-1">Short Answer</button>
                </div>
            </div>
            <QuestionBox header="Question:"></QuestionBox>

            </Box>
        </div>
    </div>
</template>

<script>
import Box from '~/components/Box.vue';
import QuestionBox from '~/components/QuestionBox.vue';

export default {
components: {
    Box,
    QuestionBox,
}}
</script>
