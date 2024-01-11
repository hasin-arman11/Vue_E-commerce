<template>
   <section class="container mt-5">
    <div v-if="products.length" class="row row-cols-3 row-cols-md-3">
      <showProduct
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </div>
    <h3 class="text-center mt-3 text-danger" v-else>Item Not Found</h3>
    </section>
</template>

<script>
import axios from 'axios';
import showProduct from './showProducts.vue'
export default {
  name: "searchProduct",
  data(){
    return{
        products:[]
    }
  },
  components:{
    showProduct
  },
  mounted(){
    if (this.search != "") {
        axios
          .get(`http://127.0.0.1:8000/items/?search=${this.$route.query.q_str}`)
          .then((res) => {
            this.products = res.data;
          })
          .catch((err) => console.log(err));
      }
  }
};
</script>

<style scoped></style>
