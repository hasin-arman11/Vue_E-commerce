<template>
  <section class="row">
    <div class="col-10">
      <section class="container">
        <div
          id="carouselExampleControls"
          class="carousel slide"
          data-ride="carousel"
        >
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img
                class="fixed-image"
                src="../assets/headphone.png"
                alt="First slide"
              />
            </div>
            <div class="carousel-item">
              <img
                class="d-block w-100"
                src="../assets/tv.png"
                alt="Second slide"
              />
            </div>
            <div class="carousel-item">
              <img
                class="d-block w-100"
                src="../assets/xbox.png"
                alt="Third slide"
              />
            </div>
          </div>
          <a
            class="carousel-control-prev"
            href="#carouselExampleControls"
            role="button"
            data-slide="prev"
          >
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a
            class="carousel-control-next"
            href="#carouselExampleControls"
            role="button"
            data-slide="next"
          >
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
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
    <div style="margin-top: 6rem;" class="col-2">
      <div class="card text-white bg-primary mb-3" style="max-width: 18rem">
        <div class="card-header">Header</div>
        <div class="card-body">
          <h5 class="card-title">Primary card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
        </div>
      </div>
      <div class="card text-white bg-success mb-3" style="max-width: 18rem">
        <div class="card-header">Header</div>
        <div class="card-body">
          <h5 class="card-title">Success card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
        </div>
      </div>
      <div class="card text-white bg-danger mb-3" style="max-width: 18rem">
        <div class="card-header">Header</div>
        <div class="card-body">
          <h5 class="card-title">Danger card title</h5>
          <p class="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
        </div>
      </div>
    </div>
  </section>
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

<style scoped>
.fixed-image {
  height: 400px;
  object-fit: contain;
  width: 100%;
  margin-top: 80px;
}
</style>
