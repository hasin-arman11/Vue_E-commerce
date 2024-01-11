<template>
  <header>
    <nav
      class="navbar bg-dark navbar-expand-lg bg-body-tertiary"
      data-bs-theme="dark"
    >
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Vue-Mart</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li v-if="this.$store.state.isAuthenticated" class="nav-item">
              <a @click="logout" style="cursor: pointer" class="nav-link"
                >Logout</a
              >
            </li>
            <li v-else class="nav-item">
              <router-link class="nav-link" to="/signup">SignUp</router-link>
            </li>
            <li v-if="this.$store.state.isAuthenticated" class="nav-item">
              <router-link class="nav-link" to="/addProduct"
                >Add Product</router-link
              >
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Category
              </a>
              <ul class="dropdown-menu">
                <li v-for="category in category_list" :key="category.id">
                  <router-link
                    class="dropdown-item"
                    :to="'/' + category.slug"
                    >{{ category.name }}</router-link
                  >
                </li>
              </ul>
            </li>
          </ul>
          <div class="d-flex" role="search">
            <input
              class="form-control me-2"
              type="search"
              v-model="searched"
              placeholder="Search"
              aria-label="Search"
            />
            <router-link :to="`/search${searched ? '?q_str=' + searched : ''}`"
              ><button class="btn btn-outline-info">Search</button></router-link
            >
          </div>
          <router-link to="/cart" class="btn btn-success ms-3">
            <span class="icon"><i class="fas fa-shopping-cart"></i></span>
            <span class="ps-1 fw-bold">Cart ({{ cartTotalLength }})</span>
          </router-link>
          <router-link v-if="!this.$store.state.isAuthenticated" to="/login" class="btn btn-info fw-bold text-white ms-3">
            Login
          </router-link>
        </div>
      </div>
    </nav>
  </header>
  <section>
    <router-view />
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      cart: {
        items: [],
      },
      searched: "",
      products: [],
      category_list: [],
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
  },
  mounted() {
    this.cart = this.$store.state.cart;
    this.get_all_category();
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;
      for (let index = 0; index < this.cart.items.length; index++) {
        totalLength += this.cart.items[index].quantity;
      }
      return totalLength;
    },
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
    get_all_category() {
      axios
        .get("http://localhost:8000/categories/")
        .then((res) => {
          this.category_list = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style></style>
