<template>
    <div class="place-self-center bg-blue2 w-1/2 rounded" >
        <div :class="`flex ${isCentered ? 'self-center' : ''}`">
            <h1 
                class="w-full text-center font-bold text-xl bg-green2 p-7 rounded">
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