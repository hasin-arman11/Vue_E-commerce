<template>
  <div>
    <h1 class="text-center text-primary">SIGNUP FORM</h1>
    <hr />
    <div style="margin-left: 430px">
      <input
        type="text"
        class="form-control w-50 mb-2"
        v-model="formValue.username"
        placeholder="Enter Username"
      />
      <input
        type="text"
        class="form-control w-50 mb-2"
        v-model="formValue.first_name"
        placeholder="Enter First Name"
      />
      <input
        type="text"
        class="form-control w-50 mb-2"
        v-model="formValue.last_name"
        placeholder="Enter Last Name"
      />
      <input
        type="email"
        class="form-control w-50 mb-2"
        v-model="formValue.email"
        placeholder="Enter Email"
      />
      <input
        type="password"
        class="form-control w-50 mb-2"
        v-model="formValue.password"
        placeholder="Enter Password"
      />
      <input
        type="password"
        class="form-control w-50 mb-2"
        v-model="formValue.confirm_password"
        placeholder="Enter Password Again"
      />
      <button class="btn btn-sm btn-secondary" @click="SignMethod">
        Submit
      </button>
      <p v-for="err in formValue.error" :key="err" class="text-danger">{{err}}</p>
      <p class="fw-bold">
        Already signed in? <router-link to="/login">Login</router-link>
      </p>
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
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        confirm_password: "",
        error:[]
      },
    };
  },
  methods: {
    SignMethod() {
      if (this.formValue.password == this.formValue.confirm_password) {
        axios
          .post("http://127.0.0.1:8000/users/",this.formValue)
          .then((response) => {
            if (response.status == 200) {
              this.$router.push({ name: "Home" });
            }
          })
          .catch((error) => {
            this.formValue.error.push(error)
          });
      }
      else{
        this.formValue.error.push('password did not matched')
      }
    },
  },
};
</script>
