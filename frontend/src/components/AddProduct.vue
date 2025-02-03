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
        <div>
          <label>Choose File</label>
          <input @change="setFile($event)" style="margin-left:20px" type="file" name="image" id="image">
        </div>
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
                    file:null
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
            setFile(event){
              this.form.file=event.target.files[0]
            },
            addProduct(event){ 
              const formData = new FormData();
              formData.append('file', this.form.file);
              formData.append('product_name', this.form.product_name);
              formData.append('category', this.form.category);
              formData.append('price', this.form.price);
              formData.append('description', this.form.description);
              

                axios.post('http://localhost:8000/products/',formData,{headers: {
                'Content-Type': 'multipart/form-data',
                }})
                .then(res=>{
                    if (res){
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