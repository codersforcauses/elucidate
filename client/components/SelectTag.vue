<template>
  <div class="relative m-1.5">
    <button @click="$emit('toggleTag', label)" :class=css>{{ label }}</button>
  </div>
</template>

<script>
export default {
  computed: {
    css : function () {
      return this.colour + " rounded";
    }
  },
  props: ['label', 'colour']
}
</script>

<style>
</style>