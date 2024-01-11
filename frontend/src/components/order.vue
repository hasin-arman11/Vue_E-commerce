<template>
  <div class="container shadow p-3 mt-5 mb-5 h-75">
    <h2 class="text-secondary">Cart</h2>
    <table class="table table-bordered  p-3" v-if="getTotalPrice[1]">
      <thead>
        <tr>
          <th scope="col">Product</th>
          <th scope="col">Price</th>
          <th scope="col">Quantity</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in cart.items" :key="item.id">
          <td>{{ item.product.product_name }}</td>
          <td>{{ item.product.price }}</td>
          <td>{{ item.quantity }}</td>
        </tr>
        <tr>
          <td colspan="4" class="fw-bold">
            Total Price
            <span style="paddingLeft: 425px">{{ getTotalPrice[0] }}$</span>
          </td>
        </tr>
      </tbody>
    </table>
    <h3 v-else>You don't have any product in cart</h3>
    <div>
      <h4 class="text-danger mt-5">Shipping Details</h4>
      <div class="row">
        <div class="col-md-5">
          <label class="fw-bold">Name*</label>
          <input class="form-control" v-model="shipping.name" type="text" />
          <br />
          <label class="fw-bold">Address*</label>
          <textarea class="form-control" v-model="shipping.address" rows="1"></textarea>
          <br />
          <label class="fw-bold">Email*</label>
          <input class="form-control" v-model="shipping.email" type="email" />
          <br />
          <label class="fw-bold">Phone*</label>
          <input class="form-control" v-model="shipping.phone" type="text" />
          <br />
          <button @click="submit_order" class="btn fw-bold btn-primary">Order</button>
        </div>
        <div class="col-md-5">
          <label class="fw-bold">State*</label>
          <input class="form-control" v-model="shipping.state" type="text" />
          <br />
          <label class="fw-bold">Country*</label>
          <input class="form-control" v-model="shipping.country" type="text" />
          <br />
          <label class="fw-bold">Post code*</label>
          <input class="form-control" v-model="shipping.post_code" type="text" />
        </div>
        <p class="text-danger" v-for="err in shipping.errors" :key="err">{{err}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
// import getheaders from '../utlities/util'
export default {
  name: "OrderPage",
  methods: {

    
    remove(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.product.id != item.product.id
      );
    },
    submit_order(){
      this.shipping.errors=[]
      if(this.shipping.name==''){
        this.shipping.errors.push('username is required')
      }
      if(this.shipping.address==''){
        this.shipping.errors.push('address is required')
      }
      if(this.shipping.email==''){
        this.shipping.errors.push('email is required')
      }
      if(this.shipping.phone==''){
        this.shipping.errors.push('phone is required')
      }
      const payload = {
          name:this.shipping.name,
          address:this.shipping.address,
          email:this.shipping.email,
          phone:this.shipping.phone,
          state:this.shipping.state,
          country:this.shipping.country,
          post_code:this.shipping.post_code,
          items:this.cart.items
        }
      if(!this.shipping.errors.length){
        axios.post('http://127.0.0.1:8000/orders/',payload)
        .then(res=>{
          if(res.status==200){
            this.$router.push({name:'success'})
          }
        })
        .catch(err=>{
          this.shipping.errors.push('Sorry!! Can not place your order.')
        })
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    getTotalPrice() {
      let total = 0;
      let count = 0;
      this.cart.items.map((item) => {
        total += item.product.price * item.quantity;
        count += item.quantity;
      });
      return [total, count];
    },
  },
  data() {
    return {
      cart: {
        items: [],
      },
      shipping:{
        name:"",
        address:"",
        email:"",
        phone:"",
        state:"",
        country:"",
        post_code:"",
        errors:[]
      }
    };
  },
};
</script>

<style scoped></style>
