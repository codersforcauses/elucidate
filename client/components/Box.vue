<template>
    <div class="absolute top-1/4 left-1/4 bg-blue w-1/2" >
        <div :class="`flex ${isCentered ? 'self-center' : ''}`">
            <h1 
                class="font-bold text-center text-3xl bg-green w-full">
                {{ title }}
            </h1>
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