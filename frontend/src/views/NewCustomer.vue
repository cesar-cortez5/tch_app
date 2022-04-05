<template>
  <div class="customerform">
    <div class="mb-3">
      <label for="fullname" class="form-label">Full Name</label>
      <input
        type="text"
        class="form-control"
        id="fullname"
        v-model="fullname"
        @blur="v$.fullname.$touch"
      />
      <div style="color: red" class="error" v-if="v$.fullname.$error">
        Name is required
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
    <div class="mb-3">
      <label for="citystate" class="form-label">City, State</label>
      <input
        type="text"
        class="form-control"
        id="citystate"
        v-model="citystate"
        @blur="v$.citystate.$touch"
      />
      <div style="color: red" class="error" v-if="v$.citystate.$error">
        A city and a state is required
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
import useValidate from "@vuelidate/core";
import { required, maxLength, numeric, minLength } from "@vuelidate/validators";
import axios from "axios";
export default {
  setup() {
    return { v$: useValidate() };
  },
  data() {
    return {
      fullname: "",
      company_name: "",
      email: "",
      address: "",
      citystate: "",
      zip: "",
      phonenumber1: "",
      phonenumber2: "",
    };
  },
  validations() {
    return {
      fullname: { required },
      company_name: {maxLength: maxLength(30)},
      email: { required },
      address: { required },
      citystate: { required },
      zip: { required },
      phonenumber1: {
        required,
        maxLength: maxLength(10),
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
    async submitForm() {
      const isFormCorrect = await this.v$.$validate();
      if (isFormCorrect){
      console.log('HELLO')
      let customer_info = {
          customer_name: this.fullname,
          company_name: this.company_name,
          email: this.email,
          address: this.address,
          citystate: this.citystate,
          zip: this.zip,
          phone1: this.phonenumber1,
          phone2: this.phonenumber2,
        }
      console.log(customer_info)
      axios
        .post("/new_customer", customer_info)
        .then((res) => {
          this.customer_id = res.data;
          let route_to = `/customer_query/?customer_name=${this.fullname}`;
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
</style>