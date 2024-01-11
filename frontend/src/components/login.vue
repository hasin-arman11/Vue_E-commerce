<template>
  <div>
    <h1 class="text-center text-primary">LOGIN FORM</h1>
    <hr />
    <div style="margin-left: 400px">
      <input
        type="text"
        class="form-control w-50 mb-2"
        v-model="formValue.username"
        placeholder="Enter Username"
      />
      <input
        type="password"
        class="form-control w-50 mb-2"
        v-model="formValue.password"
        placeholder="Enter Password"
      />
      <button style="marginLeft:200px" class="btn fw-bold btn-sm btn-secondary" @click="loginMethod">
        Login
      </button>
      <p class="text-danger">{{formValue.error}}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data() {
    return {
      formValue: {
        username: "",
        password: "",
        error:""
      },
    };
  },
  methods: {
    loginMethod() {
        axios
        .post(
          `http://localhost:8000/api/token/`,this.formValue
        )
        .then((response) => {
          const token=response.data.access
          this.$store.commit("setToken",token)
          localStorage.setItem('token',token)
          const toPath = this.$route.query.to || '/cart'
          this.$router.push(toPath)

        })
        .catch((error) =>{
            console.log(error)
            this.formValue.error="Invalid password or username"
        });
    },
  },
};
</script>
