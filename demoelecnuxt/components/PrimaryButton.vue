<template>
        <button class="btn"><nuxt-link :to="topage">{{action}}</nuxt-link></button>
</template>
<script>
export default {
    props:{
        topage:{
            type:String,
            default:''
        },
        action:{
            type:String,
            required:true
        }
    }
}
</script>
<style>
.btn{
  background: dodgerblue;
  border-radius: 5px;
  border: dodgerblue;
  height: 30px;
  color: #ffffff;
  font-weight: bold;
  box-shadow: 0 5px 5px rgb(165, 165, 238);
}
</style>