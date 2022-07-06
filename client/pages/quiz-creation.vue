<template>
    <div class="flex flex-grow flex-col items-center content-center">
            <div>
                <div class="flex place-content-center bg-green">
                    <h1 class="text-center text-3xl font-bold">Create a quiz</h1>
                </div>
                <Box>
                    <TextBox header="Quiz Name" inputType="text" />
                    <TextBox header="Tags" inputType="text"/>
                    <TextBox header="Time Limit" inputType="number"/>
                </Box>
            </div>

    </div>
</template>

<script>
import Box from '~/components/Box.vue';

export default {
  components: {
    Box,
  },
};
</script>