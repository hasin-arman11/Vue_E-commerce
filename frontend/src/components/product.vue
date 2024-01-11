<template>
  <div class="container mt-3">
    <div class="card p-3 mx-auto w-75 mb-3">
      <div class="card-body">
        <h5 class="card-title">Product Name: {{ product.product_name }}</h5>
        <p class="card-text">Description: {{ product.description }}</p>
        <p class="card-text">Product Price: ${{ product.price }}</p>
        <div class="d-flex">
          <p style="paddingright: 10px; paddingtop: 10px">Amount:</p>
          <input
            v-model="quantity"
            min="1"
            style="width: 60px"
            class="form-control"
            type="number"
          />
        </div>
        <button
          @click="addToCart"
          class="btn btn-sm fw-bold text-white btn-info mt-2"
        >
          Add to Cart
        </button>
      </div>
      <router-link :to="'/update/'+ product.id">
        <button class="btn btn-success fw-bold">Update</button>
      </router-link>
      <button @click="deleteProduct(product.id)" class="btn btn-danger fw-bold mt-2" style="width:80px">Delete</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProductDetails",
  data() {
    return {
      quantity: 1,
      product: {},
    };
  },
  mounted() {
    this.get_product();
  },
  methods: {
    deleteProduct(id){
      axios.delete(`http://localhost:8000/update/${id}/`)
      .then(res=>{
        this.$router.push('/')
      })
    },
    get_product() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;
      axios
        .get(`http://127.0.0.1:8000/${category_slug}/${product_slug}/`)
        .then((response) => {
          console.log(response);
          this.product = response.data[0];
        })
        .catch((error) => console.log(error));
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }
      const item = {
        product: this.product,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item);
    },
  },
};
</script>

<style scoped></style>
