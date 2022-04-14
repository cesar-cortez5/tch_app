<template>
    <div class="mb-3">
      <label for="state_name" class="form-inline">State Name</label>
      <!-- The v-model attribute is used to reactively connect the text within the form, and variables within the <script> tag
        This allows us to validate the form to make sure is not empty, and also get the information after the submit button is clicked
        
        The @blur attribute executes a command after an element has lost focused. For instance, if you have clicked on a textbox,
        then click on another textbok, then it will execute
        In this case, it executes v$.fullnae.$touch, which is a function that validates the form using the rules defined below.-->
      <input
        type="text"
        class="form-inline"
        id="state_name"
        v-model="state_name"
        @blur="v$.state_name.$touch"
      />
      <label for="state_abbreviation" class="form-inline">State Abbreviation</label>
      <input
        type="text"
        class="form-inline"
        id="state_abbreviation"
        v-model="state_abbreviation"
        @blur="v$.state_abbreviation.$touch"
      />

    </div>

</template>
<script>
import axios from "axios";

export default {
  //The data() function initializes an empty string
  name: "States",
  data() {
    return {
      msg: "",
      state_name: "",
      state_abbreviation: ""
    };
  },
  methods: {
    //Function that is called when web page is loaded
    deleteState(event){
        console.log(event.target.value)
        let state = event.target.value
        axios.delete("/delete_state", {params : {
          id: state
        }})
      
    },
    newState(){
        axios.post("/new_state", null, {params : {
          state_name: this.state_name,
          state_abbreviation: this.state_abbreviation
        }})
      
    },
    getStates() {
      axios
      //Sending a GET request with axios, with the customer name retrieved from the URL as the params.
        .get("/states")
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
    this.getStates();
  },
};
</script>
