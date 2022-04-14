<!-- Now this is a scary one -->

<template>
  <!-- Using form template from the bootstrap website -->
  <div class="customerform">
    <div class="mb-3">
      <label for="benchnumber" class="form-label">Bench Number</label>
      <!-- The v-model attribute is used to reactively connect the text within the form, and variables within the <script> tag
        This allows us to validate the form to make sure is not empty, and also get the information after the submit button is clicked
        
        The @blur attribute executes a command after an element has lost focused. For instance, if you have clicked on a textbox,
        then click on another textbok, then it will execute
        In this case, it executes v$.fullnae.$touch, which is a function that validates the form using the rules defined below.-->
      <input
        type="text"
        class="form-control"
        id="benchnumber"
        v-model="benchnumber"
        @blur="v$.benchnumber.$touch"
      />
            <div style="color: red" class="error" v-if="v$.benchnumber.$error">
        Bench number is necessary
      </div>

      <div class="mb-3">

      <label for="encryption" class="form-label">Encryption</label>
      <input
      
        type="text"
        class="form-control"
        id="encryption"
        v-model="encryption"
        @blur="v$.encryption.$touch"
      />
      </div>
          <div class="mb-3">
      <label for="brand" class="form-label">Brand</label>
      <input
        type="text"
        class="form-control"
        id="brand"
        v-model="brand"
        @blur="v$.brand.$touch"
      />
      </div>
      <!-- This div only shows up if an error occurs
      We accomplish this using the v-if attribute. Then, the v$.fullname.error is a boolean (True or False) -->
      <div style="color: red" class="error" v-if="v$.brand.$error">
        First Name is required
      </div>

      <div style="color: red" class="error" v-if="v$.encryption.$error">
        Last Name is required
      </div>
    </div>
    <div class="mb-3">
      <label for="loginuser" class="form-label">Login User</label>
      <input
        type="text"
        class="form-control"
        id="loginuser"
        v-model="loginuser"
        @blur="v$.loginuser.$touch"
      />

    </div>
    <div class="mb-3">
      <label for="loginpassword" class="form-label">Login Password</label>
      <input
        type="text"
        class="form-control"
        id="loginpassword"
        v-model="loginpassword"
        @blur="v$.loginpassword.$touch"
      />

    </div>
    <div class="mb-3">
      <label for="operatingsystem" class="form-label">Operating System</label>
      <input
        type="text"
        class="form-control"
        id="operatingsystem"
        v-model="operatingsystem"
        @blur="v$.operatingsystem.$touch"
      />

    </div>
    <div class="mb-3">
      <label for="model" class="form-label">Model</label>
      <input
        type="text"
        class="form-control"
        id="model"
        v-model="model"
        @blur="v$.model.$touch"
      />

    </div>

    <div class="mb-3">
      <label for="pin" class="form-label">PIN</label>
      <input
        type="text"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*?)\..*/g, '$1');"
        class="form-control"
        id="pin"
        v-model="pin"
        @blur="v$.pin.$touch"
      />
      <div style="color: red" class="error" v-if="v$.pin.$error">
        A zip code is required.
      </div>
    </div>
    <div class="mb-3">
      <label for="serialnumber" class="form-label">Serial Number</label>
      <!-- The oninput attribute contains a javascript command that on the fly deletes any character that is not a number -->
      <input
        type="text"
        class="form-control"
        id="serialnumber"
        v-model="serialnumber"
        @blur="v$.serialnumber.$touch"
      />
      <div style="color: red" class="error" v-if="v$.serialnumber.$error">
        Error with serial number
      </div>
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
      loginuser: "",
      loginpassword: "",
      encryption: "",
      brand: "",
      model: "",
      benchnumber: "",
      operatingsystem: "",
      pin: "",
      serialnumber: "",
      status: "",
      customer_id: ""
    };
  },
  validations() {
    return {
      //The required tag throws an error if a textbox is empty
      loginuser: {  },
      loginpassword: {},
      //The maxLength tag makes sure that a textbox does not go over 30 characters long
      encryption : {},
      brand: {maxLength: maxLength(30)},
      model: {  },
      benchnumber: { required },
      operatingsystem: {  },
      pin: {
        
      },
      serialnumber: {
        
      },
    };
  },
  methods: {
    //This function is run after the submit button is clicked
    //Async is used here as it is retrieving the data from the form on the fly, and the data could change if there is an error.

     onChangeStatus(event) {
      console.log(event.target.value)
      this.status = event.target.value
    },
    getStates() {
      axios.get("/status_types").then((res) => {
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
      /*let customer_info = {
          loginuser: this.loginuser,
          loginpassword: this.loginpassword,
          encryption: this.encryption,
          brand: this.brand,
          model: this.model,
          bench_number: this.benchnumber,
          operatingsystem: this.operatingsystem,
          serialnumber: this.serialnumber,
          customer_id : this.customer_id,
          pin: this.pin,
          invoice_status_id: 1,
          invoice_date: new Date().toISOString().slice(0, 10)
        }*/
        let customer_info = {
          bench_number: this.benchnumber,
          invoice_date: new Date().toISOString().slice(0, 10),
          invoice_status_id: 3,
          loginuser: this.loginuser,
          loginpassword: this.loginpassword,
          encryption: this.encryption,
          brand: this.brand,
          model: this.model,
          operatingsystem: this.operatingsystem,
          serialnumber: this.serialnumber,
          customer_id: this.$route.query.customerId,
          pin: this.pin
        }

      console.log(customer_info)
      //Making a post request to the /new_customer endpoint from our backend, with customer_info variable as a payload
      axios
        .post("/new_invoice", customer_info)
        .then((res) => {
          //Getting the data from the request. In this case, the endpoint returns a customer id
          this.invoice_id = res.data.invoice_id;
          this.equipment_id = res.data.equipment_id;
          //After the axios request is done, it then redirects the webpage to the customer_queyr page. For more information on this, look at
          //the ReturningCusomer.vue file, and also the router/index.js file
          let route_to = `/customer_page/?customer_id=${this.$route.query.customerId}`;
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