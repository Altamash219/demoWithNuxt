<template>
    <div class="flex">
        <burger-image :orderImage="order.image"/>
        <burger-content :ingridient="ingridients" class="mt-24"/>
    </div>

</template>

<script>
import BurgerImage from "~/components/BurgerImage";
import BurgerContent from "~/components/BurgerContent";
export default {
    components:{
        BurgerImage,
        BurgerContent
    },
    data(){
    return{
        order:{
            name:"Burger1",
            image:'burger.png',
            price: '$10' 
        },
            ingridients:[
                {
                    name:"Cheese",
                    image:'burger.png',
                    price: '$10'   
                },
                {
                    name:"Tomato",
                    image:'burger.png',
                    price: '$10'   
                },
                {
                    name:"Onion",
                    image:'burger.png',
                    price: '$10'   
                },
                {
                    name:"Mayonaisse",
                    image:'burger.png',
                    price: '$10'   
                }
            ]
          
        }
    }
}
</script>

<style>

</style>