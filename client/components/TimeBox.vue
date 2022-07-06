<template>
    <div>
        <label class="text-white text-xl font-bold">{{ header }}</label>
        <input type="time">
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
