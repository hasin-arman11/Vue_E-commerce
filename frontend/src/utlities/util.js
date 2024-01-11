export default function getheaders(){
    const token = localStorage.getItem('token')
    if(token){
      return { 'Authorization' : 'Bearer ' + token}
    }else{
      return {}
    }

}