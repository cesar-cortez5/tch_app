<template>
<!-- Creating buttons to make a new user, and search for a user.
These butotons link to the new_customer and returning_customer files within the frontend/src/views folder-->
  <div class="all_buttons">
    <!-- router-link is used to redirect when the button is clicked -->
    <router-link to="/states" tag="button" class="btn btn-primary btn-lg" id=homebuttons>States</router-link>
    <router-link to="/countries" tag="button" class="btn btn-primary btn-lg" id=homebuttons>Countries</router-link>
    <router-link to="/Cust_ContactTable" tag="button" class="btn btn-primary btn-lg" id=homebuttons>Customer Contact</router-link>
    <router-link to="/Emp_ContactTable" tag="button" class="btn btn-primary btn-lg" id=homebuttons>Employee Contact</router-link>
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