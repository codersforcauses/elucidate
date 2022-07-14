<template>
  <div>
    <input type="checkbox" :checked="selected" @click="$emit('toggleTag', label)" />
    <label>
      {{ label }}
    </label>
  </div>
</template>

<script>
export default {
  props: ['label', 'selected']
}
</script>

<style>
</style>