<template>
    <div class="mb-5 ml-20">
        <label class="p-10 text-white text-xl font-bold"><font-awesome-icons icon="fa-regular fa-stopwatch"/>{{ header }}</label>
        <input class="p-0 m-0 w-1/2 h-9 rounded shadow-sm" type="time">
    </div>
</template>

<script>
export default {
    name: 'TimeBox',
    props: {
        header: String,

    }
}
</script>
