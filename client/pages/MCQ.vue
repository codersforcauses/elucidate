<template>
    <div>
        <h1>Create A Quiz</h1>
        <div>
            <Box title="{Display Quiz Name}" :is-centered="false">

            <div>
                <p class="flex inline-flex">Question Type:</p>
                <button class="flex inline-flex">Multiple Choice</button>
                <button class="flex inline-flex">Short Answer</button>
            </div>

            <TextBox header="Question:"></TextBox>

            </Box>
        </div>
    </div>
</template>

<script>
import Box from '~/components/Box.vue';
import TextBox from '~/components/TextBox.vue';

export default {
components: {
    Box,
    TextBox,
}}
</script>
