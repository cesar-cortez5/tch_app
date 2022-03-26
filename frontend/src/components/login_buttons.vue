<template>
  <div class="all_buttons">
    <router-link to="/new_customer" tag="button" class="btn btn-primary btn-lg" id=homebuttons>New Customer</router-link>
    <router-link to="/returning_customer" tag="button" class="btn btn-primary btn-lg" id=homebuttons>Returning Customer</router-link>

  </div>
  


</template>

<style scoped>
.all_buttons {
  padding: 5px;
  text-align: center;

  
}
#homebuttons {
  margin: 5px;
}
</style>