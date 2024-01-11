<template>
  <div class="container">
    <h2 class="text-center text-success">Cart</h2>
    <table class="table table-bordered shadow" v-if="getTotalPrice[1]">
      <thead>
        <tr>
          <th scope="col">Product</th>
          <th scope="col">Price</th>
          <th scope="col">Quantity</th>
          <th scope="col">Total</th>
        </tr>
      </thead>
      <tbody>
        <CartItems @removeItem="remove"  v-for="item in cart.items" :key="item.id" :initialItem="item"/>
      </tbody>
    </table>
    <h3 v-else>You don't have any product in cart</h3>
    <h3 class="text-center text-warning">Summary</h3>
    <hr class="text-danger">
    <h5>Total Price: <span class="text-info">{{getTotalPrice[0]}}</span></h5>
    <h5>Quantity: <span  class="text-info">{{getTotalPrice[1]}}</span></h5>
    <router-link to="/order"><button class="btn btn-success mt-3">Checkout</button></router-link>
  </div>
</template>

<script>
import CartItems from './CartItems.vue'
export default {
  name: "cartPage",
  components:{
    CartItems
  },
  methods:{
    remove(item){
        this.cart.items=this.cart.items.filter( i => i.product.id != item.product.id)
    }
  },
  mounted(){
    this.cart=this.$store.state.cart
  },
  computed:{
    getTotalPrice(){
        let total=0
        let count=0
        this.cart.items.map(item=>{
            total+=item.product.price*item.quantity
            count+=item.quantity
        })
        return [total,count]
    }
  },
  data(){
    return{
        cart:{
            items:[]
        }
    }
  }
};
</script>

<style scoped></style>
