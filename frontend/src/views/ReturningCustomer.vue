<template>
  <div id="customer_search" class="input-group mb-3">
    <!-- Search bar design taken from Bootstrap -->
    <input
      type="search"
      class="form-control rounded"
      placeholder="Enter Customer Name..."
      aria-label="Search"
      aria-describedby="search-addon"
      v-model="customer_name"
    />
    <!-- The @click attribute activates when the button is clicked. In this case, it runs the search_customer() function defined at the bottom of this file -->
    <button type="button" @click="search_customers" class="btn btn-primary btn-lg">Search</button>
  </div>
</template>

<style>
#customer_search {
  padding-left: 5%;
  padding-right: 5%;
  padding-top: 5%;
}
</style>

<script>

export default{
  setup() {
    
  },
  data(){
    return {
        customer_name: ""
    }
  },
  methods: {
    search_customers() {
      //Redirecing to customer query, with customer name as a parameter
      let route_to = `/customer_query/?customer_name=${this.customer_name}`;
      this.$router.push(route_to)
    }
    
  }
}
</script>
