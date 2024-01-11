<template>
  <div>
    <section class="container">
      <img
        src="../assets/6505894.jpg"
        class="img-fluid w-100"
        style="height: 400px"
        alt=""
      />
    </section>
    <h1 class="text-center mb-5 text-primary mt-2">Latest Products</h1>
    <section class="container mb-5">
      <div class="row row-cols-3 row-cols-md-3 gy-4">
        <showProduct
          v-for="product in products"
          :key="product.id"
          :product="product"
        />
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import showProduct from "./showProducts.vue";
export default {
  name: "HomePage",
  data() {
    return {
      products: [],
    };
  },
  components: {
    showProduct,
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/products/")
      .then((response) => {
        this.products = response.data;
      })
      .catch((error) => console.log(error));
  },
};
</script>

<style scoped></style>
