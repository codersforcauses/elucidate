<template>
    <div class="flex flex-inline mb-20 mx-10">
        <label class="flex align-text-top p-10 text-white text-xl font-bold">{{ header }}</label>
        <input class="p-0 m-0 w-3/4 h-27 rounded shadow-sm" :type="inputType" />
    </div>
</template>

<script>
export default {
    name: 'QuestionBox',
    props: {
        header: String,
        inputType: String
    }
}
</script>

