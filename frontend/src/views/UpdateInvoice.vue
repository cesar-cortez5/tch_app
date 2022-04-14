<template>
  <div>
    <h3> Change Invoice Status </h3>
    <select
      @click="getStatus"
      class="form-select"
      aria-label="State"
      id="statedropdown"
    >
      <option
        v-for="status in msg.statuses"
        :key="status.Status_ID"
        :value="status.Status_ID"
        @click="onChangeState(status.Status_ID)"
      >
        {{ status.Status_Name }}
      </option>
    </select>
  </div>
</template>

<script>
import axios from "axios";

export default {
  setup() {},
  data() {
    return {
      msg: "",
      status: "",
    };
  },
  methods: {
    getStatus() {
      axios
        .get("/status_types")
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    onChangeState(status_id) {
      this.status = parseInt(status_id);
      console.log(this.status)
      console.log(this.$route.query)
      axios
        .get("/update_status",{ crossDomain: true },{params: 
        {invoice_id: parseInt(this.$route.query.invoiceId),
        invoice_status_id: this.status}})
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);

        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>