<template>
    <div class="place-self-center bg-blue w-1/2" >
        <div :class="`flex ${isCentered ? 'self-center' : ''}`">
            <h1 
                class="w-full text-center font-bold text-xl bg-green p-7">
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