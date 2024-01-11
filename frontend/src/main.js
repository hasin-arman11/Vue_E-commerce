import { createApp } from 'vue'
import App from './App.vue'
import router from './routers'
import 'bootstrap/dist/css/bootstrap.css'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
import store from './store/index.js'
import axios from 'axios'
createApp(App).use(bootstrap).use(store).use(router).mount('#app')

axios.interceptors.request.use(config => {
    console.log('request----->',config)
    const get_token = store.state.token
    if (get_token){
        config.headers.Authorization = `Bearer ${get_token}`
    }
    return config
})

axios.interceptors.response.use((response)=> response,(error)=>{
    console.log('response error---->',error)
    if (error.response){
        if (error.response.status == 401){
            localStorage.removeItem('token')
            store.state.isAuthenticated=false
            router.push('/login')
        }
        else{
            alert('An error occurred. Please try again later.')
        }
    }
})