<template>
  <div>
    <h3> Change Invoice Status </h3>
    <select
      @change="onChangeState($event)"

      class="form-select"
      aria-label="State"
      id="statedropdown"
    >
      <option
        v-for="status in msg.statuses"
        :key="status.Status_ID"
        :value="status.Status_ID"
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
    onChangeState(event) {
      let status_id = event.target.value
      this.status = parseInt(status_id);
      console.log(this.status)
      console.log(this.$route.query)
      let invoice_params = {
        invoice_id : parseInt(this.$route.query.invoiceId),
        invoice_status_id: this.status
      }
      console.log(invoice_params)
      axios
        .post("/update_status", invoice_params)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);

        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getStatus();
  }
};
</script>