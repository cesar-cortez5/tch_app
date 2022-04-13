<!-- Now this is a scary one -->

<template>
  <!-- Using form template from the bootstrap website -->
  <div class="customerform">
    <div class="mb-3">
      <label for="firstname" class="form-inline">First Name</label>
      <!-- The v-model attribute is used to reactively connect the text within the form, and variables within the <script> tag
        This allows us to validate the form to make sure is not empty, and also get the information after the submit button is clicked
        
        The @blur attribute executes a command after an element has lost focused. For instance, if you have clicked on a textbox,
        then click on another textbok, then it will execute
        In this case, it executes v$.fullnae.$touch, which is a function that validates the form using the rules defined below.-->
      <input
        type="text"
        class="form-inline"
        id="firstname"
        v-model="firstname"
        @blur="v$.firstname.$touch"
      />
      <label for="middleinitial" class="form-inline">Middle Initial</label>
      <input
        type="text"
        class="form-inline"
        id="middleinitial"
        v-model="middleinitial"
        @blur="v$.middleinitial.$touch"
      />
      <label for="lastname" class="form-inline">Last Name</label>
      <input
        type="text"
        class="form-inline"
        id="lastname"
        v-model="lastname"
        @blur="v$.lastname.$touch"
      />
      <!-- This div only shows up if an error occurs
      We accomplish this using the v-if attribute. Then, the v$.fullname.error is a boolean (True or False) -->
      <div style="color: red" class="error" v-if="v$.firstname.$error">
        First Name is required
      </div>
      <div style="color: red" class="error" v-if="v$.middleinitial.$error">
        Middle initial needs to be exactly 1 character
      </div>
      <div style="color: red" class="error" v-if="v$.lastname.$error">
        Last Name is required
      </div>
    </div>
    <div class="mb-3">
      <label for="companyname" class="form-label">Company Name</label>
      <input type="text" class="form-control" id="companyname" />
    </div>
    <div class="mb-3">
      <label for="email" class="form-label">E-Mail</label>
      <input
        type="text"
        class="form-control"
        id="email"
        v-model="email"
        @blur="v$.email.$touch"
      />
      <div style="color: red" class="error" v-if="v$.email.$error">
        Email is required
      </div>
    </div>
    <div class="mb-3">
      <label for="address" class="form-label">Address</label>
      <input
        type="text"
        class="form-control"
        id="address"
        v-model="address"
        @blur="v$.address.$touch"
      />
      <div style="color: red" class="error" v-if="v$.address.$error">
        Address is required
      </div>
    </div>

          <div class="row">
              <div class="col-sm-6">
                  <div class="form-group">
          <select @click="getStates" @change="onChangeState($event)" class="form-select" aria-label="State" id="statedropdown">
                          <option v-for="state in msg.states" :key="state.State_Name" :value = "state.State_ID">{{state.State_Name}}</option>
                      </select>
                  </div>
              </div>
              <div class="col-sm-6">
                  <div class="form-group">
          <select  @click="getCountries" @change="onChangeCountry($event)" class="form-select" aria-label="Country" id="countrydropdown">
            <option v-for="country in msg.countries" :value = "country.Country_ID">{{country.Country_Name}}</option>
                      </select>
                  </div>
              </div>
          </div>
    <div class="mb-3">
      <label for="zip" class="form-label">Zip</label>
      <input
        type="number"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
        class="form-control"
        id="zip"
        v-model="zip"
        @blur="v$.zip.$touch"
      />
      <div style="color: red" class="error" v-if="v$.zip.$error">
        A zip code is required.
      </div>
    </div>
    <div class="mb-3">
      <label for="phonenumber1" class="form-label">Phone #1</label>
      <!-- The oninput attribute contains a javascript command that on the fly deletes any character that is not a number -->
      <input
        type="number"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
        class="form-control"
        id="phonenumber1"
        v-model="phonenumber1"
        @blur="v$.phonenumber1.$touch"
      />
      <div style="color: red" class="error" v-if="v$.phonenumber1.$error">
        Your phone number needs to be exactly 10 digits
      </div>
    </div>

    <div class="mb-3">
      <label for="phonenumber2" class="form-label">Phone #2</label>
      <input
        type="number"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
        class="form-control"
        id="phonenumber2"
      />
    </div>
    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="validator" />
      <label class="form-check-label" for="validator"
        >I have confirmed all the information is correct.</label
      >
    </div>
    <div v-if="!v$.$error">
      <button @click="submitForm" class="btn btn-primary">Submit</button>
    </div>
  </div>
</template>

<script>
//I am using vuelidate to validate forms. More info here https://vuelidate-next.netlify.app/
import useValidate from "@vuelidate/core";
import { required, maxLength, numeric, minLength } from "@vuelidate/validators";
//Axios for API calls
import axios from "axios";
export default {
  //This setup is ran at the start. The v$:use validate() creates a new isntance of vuelidate
  setup() {
    return { v$: useValidate() };
  },
  //Creating new variables that will be retrieved from the form
  data() {
    return {
      firstname: "",
      lastname: "",
      middleinitial: "",
      company_name: "",
      email: "",
      address: "",
      city: "",
      state: "",
      zip: "",
      selected_country: "",
      phonenumber1: "",
      phonenumber2: "",
      msg: ""
    };
  },
  validations() {
    return {
      //The required tag throws an error if a textbox is empty
      firstname: { required },
      middleinitial: {maxLength: maxLength(1)},
      //The maxLength tag makes sure that a textbox does not go over 30 characters long
      lastname : {required},
      company_name: {maxLength: maxLength(30)},
      email: { required },
      address: { required },
      zip: { required },
      phonenumber1: {
        required,
        maxLength: maxLength(10),
        //The numeric tag makes sure that the input is only numbers
        numeric: numeric,
        minLength: minLength(10),
      },
      phonenumber2: {
        maxLength: maxLength(10),
        numeric: numeric,
        minLength: minLength(10),
      },
    };
  },
  methods: {
    //This function is run after the submit button is clicked
    //Async is used here as it is retrieving the data from the form on the fly, and the data could change if there is an error.
    onChangeState(event) {
      console.log(event.target.value)
      this.state = event.target.value
    },
    onChangeCountry(event) {
      this.selected_country = event.target.value
    },
    getStates() {
      axios.get("/states").then((res) => {
        this.msg = res.data
        console.log(this.msg)
      })
      .catch((error) => {
        console.log(error)
      });
    },
    getCountries() {
      axios.get("/countries").then((res) => {
        this.msg = res.data
        console.log(this.msg)
      })
      .catch((error) => {
        console.log(error)
      });
    },
 
    async submitForm() {
      //This variable validates the form, and returns a JSON object that contains any errors that occured
      const isFormCorrect = await this.v$.$validate();
      //If no errors, then the following code will run
      if (isFormCorrect){
      console.log('HELLO')
      //The customer_info JSON will be send to the customer_query api as a payload
      let customer_info = {
          first_name: this.firstname,
          middle_initial: this.middleinitial,
          last_name: this.lastname,
          company_name: this.company_name,
          email: this.email,
          address: this.address,
          city: this.city,
          state: this.state,
          zip: this.zip,
          country: this.selected_country,
          phone1: this.phonenumber1,
          phone2: this.phonenumber2,
        }
      console.log(customer_info)
      //Making a post request to the /new_customer endpoint from our backend, with customer_info variable as a payload
      axios
        .post("/new_customer", customer_info)
        .then((res) => {
          //Getting the data from the request. In this case, the endpoint returns a customer id
          this.customer_id = res.data.customer_id;
          //After the axios request is done, it then redirects the webpage to the customer_queyr page. For more information on this, look at
          //the ReturningCusomer.vue file, and also the router/index.js file
          let route_to = `/customer_query_id/?customerId=${this.customer_id}`;
          this.$router.push(route_to)
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
  },
};
</script>
 




<style>
.customerform {
  margin: 20px;
  justify-content: center;
}
#firstname {
  margin-right: 10px;
  margin-left: 10px;
  width: 30%
}
#middleinitial {
  margin-right: 10px;
  margin-left: 10px;
  width: 5%
}
#lastname {
  margin-right: 10px;
  margin-left: 10px;
  width: 30%
}
#statebutton, #countrybutton {
  margin: 5px;
}


.dropdown-menu {         
  max-height: 300px;
  overflow-y: auto;
}



</style>