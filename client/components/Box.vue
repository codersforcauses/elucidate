<template>
    <div class="mx-50 place-items-center">
        <div :class="`flex ${isCentered ? 'self-center' : ''}`">
                <h1 
                    class="w-full text-center font-bold text-xl bg-green2 p-7 rounded-tl rounded-tr">
                    {{ title }}
                </h1>
        </div>

        <div class="place-self-center bg-blue2 rounded-br rounded-bl w-fit" >
        <slot></slot>
        </div>
            
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