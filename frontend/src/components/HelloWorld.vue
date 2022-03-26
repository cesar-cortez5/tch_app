<script setup>
import login_buttons from '@/components/login_buttons.vue'
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <header>
  </header>
  <div class="greetings">
      <img alt="The Computer Hospital Logo" class="logo" src="@/assets/tch_logo.png" />


    <login_buttons></login_buttons>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}


</style>
