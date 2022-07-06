<template>
    <div>
        <label class="text-white text-xl font-bold">{{ header }}</label>
        <input :type="inputType" />
    </div>
</template>

<script>
export default {
    name: 'TextBox',
    props: {
        header: String,
        inputType: String
    }
}
</script>
