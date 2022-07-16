<template>
    <div class="mb-5 pl-20">
        <div class="flex columns-2">
        <label class="flex self-center p-10 text-white text-xl font-bold">{{ header }}</label>
        <div class="block">
        <input class="p-0 my-2 w-2/3 h-9 rounded shadow-sm" :type="inputType" />
        <input class="p-0 my-2 w-2/3 h-9 rounded shadow-sm" :type="inputType" />
        <input class="p-0 my-2 w-2/3 h-9 rounded shadow-sm" :type="inputType" />
        </div>
        </div>


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
