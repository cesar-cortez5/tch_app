<template>
  <div>
    <!-- Design is taken from boostrap. Basically, this code is a list, and for each customer it creates a row with a button next to it.-->
    <button id="new_invoice" class="btn btn-primary btn-sm" @click="newInvoice">New Invoice</button>

    <h3> Past Invoices </h3>
    <ul class="list-group" id="customers">
      <li class="list-group-item" v-for="invoice in msg.invoices" :value="invoice.Invoice_ID" :key="invoice.Invoice_ID">
            Bench Number: {{invoice.Bench_Number}} | Brand: {{invoice.Brand}} | Status: {{invoice.Equipment_Name}} ({{invoice.Status_Name}})
            <button id="customer_button" class="btn btn-primary btn-sm" :value = "invoice.Invoice_ID" @click="editInvoice($event)">Edit</button>
            <button id="customer_button" class="btn btn-danger btn-sm" :value = "invoice.Invoice_ID" @click="deleteInvoice($event)">Delete</button>
            
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
    
    newInvoice() {
      
        let route_to = `/new_invoice/?customerId=${this.$route.query.customer_id}`;
        this.$router.push(route_to)
    },
    editInvoice(event) {
        console.log(event.target.value)
        let invoice = event.target.value
        this.$router.push({ name: 'update_status', query: { invoiceId: invoice}})
    },
    deleteInvoice(event){
        console.log(event.target.value)
        let invoice = event.target.value
        axios.delete("/delete_invoice", {params : {
          id: invoice
        }})
    },

    //Function that is called when web page is loaded
    getMessage() {
      axios
      //Sending a GET request with axios, with the customer name retrieved from the URL as the params.
        .get("/invoices", { params: { customer_id: this.$route.query.customer_id} })
        .then((res) => {
        //After the request, we set the data retrieved equal to the variable we initialized earlier
          this.msg = res.data;
          console.log(this.msg)
        })
        //Logging any errors that occured. To view the logs, visit the webpage and press F12
        .catch((error) => {
          console.error(error);
        });
    },
  },
  //I dont know what this does lol
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>
#customer_button, #new_invoice{
    margin-left: 10px;
}

</style>