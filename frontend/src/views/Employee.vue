<template>
  <div id="login" class="input-group mb-3">
    <!-- Search bar design taken from Bootstrap -->
    <input
      type="username"
      class="form-control rounded"
      placeholder="Username"
      aria-label="username"
      aria-describedby="username-addon"
      v-model="username"
      id="userinput"
    />
        <input
      type="password"
      class="form-control rounded"
      placeholder="Password"
      aria-label="password"
      aria-describedby="password-addon"
      v-model="password"
      id="userpassword"
    />
    
    <!-- The @click attribute activates when the button is clicked. In this case, it runs the search_customer() function defined at the bottom of this file -->
    <button type="button" @click="login" class="btn btn-primary btn-lg">Login</button>

  </div>
</template>

<script>
import axios from "axios";

export default{
    
  setup() {
    
  },
  data(){
    return {
        username: "",
        password: "",
        authorized: false
    }
  },
  methods: {
    login() {
      axios
        .post("/employee_login", {username: this.username, password: this.password})
        .then((res) => {
          //Getting the data from the request. In this case, the endpoint returns a customer id
          this.result = res.data;
          //After the axios request is done, it then redirects the webpage to the customer_queyr page. For more information on this, look at
          //the ReturningCusomer.vue file, and also the router/index.js file
          if (this.result.authorized) {
            let route_to = '/home'
            this.$router.push(route_to)
            
          } else {
              this.authorized = true
          }

        })


    }
    
  }
}
</script>

<style>
#login {
  padding-left: 5%;
  padding-right: 5%;
  padding-top: 5%;
}
#userinput {
    margin-right:10px;
}
.disclaimer {
    margin-top: -100px;
}

</style>
