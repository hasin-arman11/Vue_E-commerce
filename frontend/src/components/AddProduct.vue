<template>
  <div>
    <h1 class="text-center text-primary">Add Product</h1>
    <hr />
    <div style="margin-left: 430px">
        <label>Name</label>
      <input
        type="text" v-model="form.product_name"
        class="form-control w-50 mb-2"
      />
        <label>Price</label>
      <input
        type="text" v-model="form.price"
        class="form-control w-50 mb-2"
      />
        <label>Description</label>
      <input
        type="text" v-model="form.description"
        class="form-control w-50 mb-2"
      />
        <label>Choose Category</label> 
        <br>

        <select  style="width: 250px" v-model="form.category">
            <option selected :value="item.id" v-for="item,index in category_list" :key="index">
                {{ item.name}}
            </option>
        </select>
        <br>
        <br>
        <button @click="addProduct" class="btn btn-primary">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
    export default {
        name:"addProduct",
        data(){
            return{ 
                form : {
                    product_name:"",
                    price:"",
                    description:"",
                    category:"",
                },
                category_list : [],
                
            }
        },
        methods:{
            get_all_category(){
               axios.get('http://localhost:8000/categories/')
               .then(res=>{
                this.category_list=res.data
               })
               .catch(err => console.log(err))
            },
            addProduct(event){ 
                axios.post('http://localhost:8000/products/',this.form)
                .then(res=>{
                    if (res.status==201){
                        this.$router.push('/')
                    }

                })
                .catch(err=>console.log(err))     
            }
        },
        mounted(){
            this.get_all_category()
        }
    }
</script>

<style scoped>

</style>