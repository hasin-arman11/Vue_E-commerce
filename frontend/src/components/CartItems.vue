<template>
    <tr>
        <td>{{initialItem.product.product_name}}</td>
        <td>{{initialItem.product.price}}</td>
        <td><button @click="increment(initialItem)" class="btn fw-bold btn-sm btn-primary">+</button> {{initialItem.quantity}} <button @click="decrement(initialItem)" class="btn btn-sm fw-bold btn-primary">-</button></td>
        <td>{{getTotal}}</td>
        <td><button class="btn btn-sm btn-danger" @click="delete_item(initialItem)">Remove</button></td>
    </tr>
</template>

<script>
    export default {
        name:'cartItems',
        props:['initialItem'],
        methods:{
            increment(item){
                item.quantity+=1
                this.update()
            },
            decrement(item){
                item.quantity-=1
                if(item.quantity==0){
                    this.delete_item(item)
                }
                this.update()
            },
            delete_item(item){
                this.$emit("removeItem",item)
                this.update()
            },
            update(){
                localStorage.setItem('cart',JSON.stringify(this.$store.state.cart))
            }
        },
        computed:{
            getTotal(){
                return this.initialItem.product.price * this.initialItem.quantity
            }
        }
    }
</script>

<style scoped>

</style>