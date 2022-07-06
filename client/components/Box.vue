<template>
    <div>
        <div :class="`flex ${isCentered ? 'place-content-center' : ''} bg-green`">
            <h1 class="text-3xl font-bold">{{ title }}</h1>
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