<template>
<!-- Creating buttons to make a new user, and search for a user.
These butotons link to the new_customer and returning_customer files within the frontend/src/views folder-->
  <div class="all_buttons">
    <!-- router-link is used to redirect when the button is clicked -->
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