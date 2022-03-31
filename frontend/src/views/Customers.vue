<template>
  <div>
    <ul class="list-group" id="customers">
      <li class="list-group-item" v-for="customer in msg.customers" :key="customer.First_Name">
            {{customer.First_Name}} {{customer.Last_Name}} ({{customer.Customer_Email}})
            <button id="customer_button" class="btn btn-primary btn-sm">Edit</button>
        </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Customers",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
      axios
        .get("/get_customer", { params: { customer_name: this.$route.query.customer_name} })
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>
#customer_button{
    margin-left: 10px;
}
</style>