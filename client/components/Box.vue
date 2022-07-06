<template>
    <div class="flex flex-col flex-grow bg-blue w-1/2" >
        <div :class="`flex ${isCentered ? 'self-center' : ''}`">
            <h1 class=" w-full bg-green text-3xl font-bold">{{ title }}</h1>
        </div>
    <slot></slot>
    </div>
</template>

<script>
export default {
    Name: 'Box',
    props: {
        title: String,
        isCentered: Boolean
    }
}
</script>