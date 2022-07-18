<template>
  <div class="h-72 w-72">
    <div class="bg-lightgrey/75 h-full">
      {{property}}
      {{propertyValue}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserAttributeCard',
  props: {
    property: {
      type: String,
      default: undefined,
    },
    propertyValue: {
      type: String,
      default: undefined,
    }

  }
};
</script>