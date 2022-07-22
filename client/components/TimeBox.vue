<template>
  <div class="flex flex-inline mb-5 ml-20">
    <label class="p-0 ml-1 mr-12 text-white text-xl font-bold">
      <FontAwesomeIcon :icon="['fa', 'stopwatch']" />
      {{ header }}
    </label>
    <input class="p-2 m-0 w-1/6 h-9 rounded shadow-sm" type="number" />
    <p class="ml-4 mr-4 text-white text-xl font-bold">mins</p>
    <input class="p-2 m-0 w-1/6  h-9 rounded shadow-sm" type="number" />
    <p class="ml-4 mr-4 text-white text-xl font-bold">secs</p>
  </div>
</template>

<script>
export default {
  name: 'TimeBox',
  props: {
    header: String,
  },
};
</script>
