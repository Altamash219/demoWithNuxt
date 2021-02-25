<template>
<div>
    <h1 class="text-3xl m-auto font-bold font-serif">Select Your Burger</h1>
    <div class="container">
        <div v-for="food in foods" :key="food.name">
            <FoodCard :food="food"/>
        </div>
    </div>
</div>
</template>

<script>
import FoodCard from '~/components/FoodCard';
// const foods = require('~/components/foods.js');
export default {
    components:{
        FoodCard
    },
    
    data(){
        return{
            foods : [
    {
        id:1,
        name:"Burger 1",
        image:'burger.png',
        price: '$10',
        number:'1'   
    },
    {
        id:2,
        name:"Burger 2",
        image:'burger.png',
        price: '$20',
        number:'2'   
    },
    {
        id:3,
        name:"Burger 3",
        image:'burger.png',
        price: '$15',
        number:'3'   
    },
    {
        id:4,
        name:"Burger 4",
        image:'burger.png',
        price: '$12',
        number:'4'   
    }
]
        }
    },
   
    

}
</script>
<style>
.container{
    display: flex;
    flex-wrap: wrap;
    overflow: hidden;
    justify-content: space-around;
    margin: auto;
}
</style>
