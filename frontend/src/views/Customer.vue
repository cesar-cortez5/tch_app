<template>
  <div>
    <!-- Design is taken from boostrap. Basically, this code is a list, and for each customer it creates a row with a button next to it.-->
    <ul class="list-group" id="current_invoices">
      <li class="list-group-item" v-for="invoice in msg.current_invoices" :key="invoice.id">
            {{customer.First_Name}} {{customer.Last_Name}} ({{customer.Customer_Email}})
            <button id="customer_button" class="btn btn-primary btn-sm">Edit_Invoice</button>
        </li>
    </ul>
  </div>
</template>

<script>
//Using axios to reference or backend API
import axios from "axios";

export default {
  //The data() function initializes an empty string
  name: "Customers",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    //Function that is called when web page is loaded
    getCurrentInvoices() {
      axios
      //Sending a GET request with axios, with the customer name retrieved from the URL as the params.
        .get("/current_invoices", { params: { customer_id: this.$route.query.customer_id} })
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
    this.getCurrentInvoices();
  },
};
</script>

<style scoped>
#customer_button{
    margin-left: 10px;
}
</style>