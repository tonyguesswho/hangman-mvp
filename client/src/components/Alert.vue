<template>
  <b-alert :variant="variant" show>{{ message }}</b-alert>
</template>

<script>
export default {
  props: ['message', 'variant'],
};
</script>
