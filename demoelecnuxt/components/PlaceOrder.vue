<template>
<div class="h-screen">
    <h1 class="text-2xl font-bold text-center capitalize">Customize Your Order</h1>
    <div class="flex-column">
        <burger-image :orderImage="order.image" class="mb-20"/>
        <h1>{{this.id}}</h1>
        <burger-content :ingridient="order.ingridients" class=""/>
    </div>
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
        id:this.$route.params.id,
        order:{
            name:"Burger1",
            image:'burger.png',
            price: '$10',
            ingridients:[
                {
                    name:"Cheese",
                    image:'burger.png',
                    price: '$10',
                    numberadd:'1',
                    numberremove:'2'   
                },
                {
                    name:"Tomato",
                    image:'burger.png',
                    price: '$10',
                    numberadd:'3',
                    numberremove:'4'      
                },
                {
                    name:"Onion",
                    image:'burger.png',
                    price: '$10',
                    numberadd:'5',
                    numberremove:'6'      
                },
                {
                    name:"Patty",
                    image:'burger.png',
                    price: '$10',
                    numberadd:'7',
                    numberremove:'8'      
                }
            ]
        }
          
        }
    }
}
</script>

<style>

</style>