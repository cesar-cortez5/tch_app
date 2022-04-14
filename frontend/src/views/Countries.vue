<template>
  <div>
    <!-- Design is taken from boostrap. Basically, this code is a list, and for each customer it creates a row with a button next to it.-->
    <ul class="list-group" id="countries">
      <li class="list-group-item" v-for="country in msg.countries" :key="country.Country_ID">
            {{country.Country_Name}}
            <button id="delete_button" class="btn btn-danger btn-sm" :value = "country.Country_ID" @click="deleteCountry($event)">Delete</button>

        </li>
        
    </ul>
  </div>
</template>

<script>
//Using axios to reference or backend API
import axios from "axios";

export default {
  //The data() function initializes an empty string
  name: "Countries",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    deleteCountry(event){
        console.log(event.target.value)
        let country = event.target.value
        axios.delete("/delete_country", {params : {
          id: country
        }})
      
    },
    //Function that is called when web page is loaded
    getCountries() {
      axios
      //Sending a GET request with axios, with the customer name retrieved from the URL as the params.
        .get("/countries")
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
    this.getCountries();
  },
};
</script>

<style scoped>
#customer_button{
    margin-left: 10px;
}
</style>