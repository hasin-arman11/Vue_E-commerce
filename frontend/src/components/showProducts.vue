<template>
  <div class="col">
    <div class="card fixed-height-card" style="width: 18rem">
      <img
        class="card-img-top fixed-image"
        :src="`http://localhost:8000/${product.file}`"
        alt="Card image cap"
      />
      <div class="card-body">
        <h5 class="card-title">{{ product.product_name }}</h5>
        <p class="card-text">{{ product.description }}</p>
        <router-link :to="product.get_absolute_url">
          <button class="btn btn-primary fw-bold">See Details</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<!-- <h5 class="card-title">{{ product.product_name }}</h5>
            <p class="card-text">
              {{ product.description }}
            </p>
            <img :src="`http://localhost:8000/${product.file}`" alt="">
            <p class="card-text">${{ product.price }}</p>
            <router-link :to="product.get_absolute_url">
              <button class="btn btn-primary fw-bold">See Details</button>
            </router-link> -->

<script>
export default {
  name: "showProduct",
  props: {
    product: Object,
  },
};
</script>

<style scoped>
.fixed-height-card {
  height: 300px;
  display: flex;
  flex-direction: column;
}

.fixed-height-card .card-body {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.fixed-image {
  height: 200px; /* Set fixed height */
  object-fit: cover; /* Ensures the image covers the area without stretching */
  width: 100%; /* Makes sure the image fills the card width */
}

</style>
