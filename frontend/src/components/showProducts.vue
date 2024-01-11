<template>
      <div class="col">
        <div class="card h-100 w-75 p-3 shadow">
          <div class="card-body">
            <h5 class="card-title">{{ product.product_name }}</h5>
            <p class="card-text">
              {{ product.description }}
            </p>
            <p class="card-text">${{ product.price }}</p>
            <router-link :to="product.get_absolute_url">
              <button class="btn btn-primary fw-bold">See Details</button>
            </router-link>
          </div>
        </div>
      </div>
</template>

<script>
export default {
  name: "showProduct",
  props: {
    product: Object,
  },
};
</script>

<style scoped></style>
