<template>
  <div>
    <!-- Design is taken from boostrap. Basically, this code is a list, and for each customer it creates a row with a button next to it.-->
    <ul class="list-group" id="customer_contact">
      <li class="list-group-item" v-for="Customer in msg.Customer_Contact" :key="Customer.customer_ID">
            Customer ID:{{Customer.Customer_ID}} Phone 1:{{Customer.Phone1}} Phone 2:{{Customer.Phone2}} Email: {{Customer.Email}}
        </li>
    </ul>
  </div>
</template>

<script>
//Using axios to reference or backend API
import axios from "axios";

export default {
  //The data() function initializes an empty string
  name: "Customer_Contact",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    //Function that is called when web page is loaded
    getCustContact() {
      axios
      //Sending a GET request with axios, with the customer name retrieved from the URL as the params.
        .get("/Cust_ContactTable")
        .then((res) => {
        //After the request, we set the data retrieved equal to the variable we initialized earlier
          this.msg = res.data;
          console.log(this.msg);
        })
        //Logging any errors that occured. To view the logs, visit the webpage and press F12
        .catch((error) => {
          console.error(error);
        });
    },
  },
  //I dont know what this does lol
  created() {
    this.getCustContact();
  },
};
</script>

<style scoped>
#customer_button{
    margin-left: 10px;
}
</style>