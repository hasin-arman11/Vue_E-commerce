<template>
  <div>
    <section class="container mt-5">
        <div class="row row-cols-3 row-cols-md-3 gy-3">
        <showProducts
            v-for="product in category.products"
            :key="product.id"
            :product="product"
        />
        </div>
    </section>
  </div>
</template>

<script>
import showProducts from './showProducts.vue'
import axios from "axios";
export default {
  name: "categoryPage",
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  components:{
    showProducts
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      const category_slug = this.$route.params.category_slug
      axios
        .get(`http://127.0.0.1:8000/${category_slug}/`)
        .then((response) => {
          this.category.products = response.data;
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped></style>
