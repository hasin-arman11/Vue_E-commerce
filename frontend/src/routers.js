import {createWebHistory,createRouter} from 'vue-router'
import Home from './components/Home.vue'
import product from './components/product.vue'
import category from './components/category.vue'
import cart from './components/cart.vue'
import signup from './components/signup.vue'
import login from './components/login.vue'
import order from './components/order.vue'
import search from './components/search_products.vue'
import success from './components/success.vue'
import addProduct from './components/AddProduct.vue'
import updateProduct from './components/update.vue'
import store from './store'
const routes=[
    {
        name:'Home',
        component:Home,
        path:'/'
    },
    {
        name:'product',
        component:product,
        path:'/:category_slug/:product_slug/'
    },
    {
        name:'category',
        component:category,
        path:'/:category_slug/'
    },
    {
        name:'update',
        component:updateProduct,
        path:'/update/:id'
    },
    {
        name:'cart',
        component:cart,
        path:'/cart'
    },
    {
        name:'signup',
        component:signup,
        path:'/signup'
    },
    {
        name:'login',
        component:login,
        path:'/login'
    },
    {
        name:'addProduct',
        component:addProduct,
        path:'/addProduct'
    },
    {
        name:'search',
        component:search,
        path:'/search'
    },
    {
        name:'success',
        component:success,
        path:'/success'
    },
    {
        name:'order',
        component:order,
        path:'/order',
        meta:{
            requireLogin:true
        }
            
    },
]

const router = createRouter({history:createWebHistory(),routes})

router.beforeEach((to,from,next)=>{
    if(to.matched.some(record =>
        record.meta.requireLogin) && !store.state.isAuthenticated)
        {
            next({name:'login',query:{to : to.path}})
        }
    else{
        next()
    }
    })
export default router