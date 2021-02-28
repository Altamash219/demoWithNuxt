<template>
<div class="h-screen">
    <h1 class="text-3xl font-bold text-center uppercase m-24">Customize Your Order</h1>
    <div class="flex-column">
        <burger-image :order="order" class="mb-20" style="height:450px"/>
        <burger-content :ingridient="order.ingridients" class="pt-20"/>
    </div>
</div>
</template>

<script>
import BurgerImage from "~/components/BurgerImage";
import BurgerContent from "~/components/BurgerContent";
import Data from "~/static/foodDetails.json";
export default {
    components:{
        BurgerImage,
        BurgerContent
    },
    data(){
    return{
        order:Data.find(burger=>this.$route.params.id==burger.id),
        // order: Data,
        // order:{
        //     name:"Burger1",
        //     image:'burger.png',
        //     price: '$10',
        //     ingridients:[
        //         {
        //             name:"Cheese",
        //             image:'burger.png',
        //             price: '$10',
        //             numberadd:'1',
        //             numberremove:'2'   
        //         },
        //         {
        //             name:"Tomato",
        //             image:'burger.png',
        //             price: '$10',
        //             numberadd:'3',
        //             numberremove:'4'      
        //         },
        //         {
        //             name:"Onion",
        //             image:'burger.png',
        //             price: '$10',
        //             numberadd:'5',
        //             numberremove:'6'      
        //         },
        //         {
        //             name:"Patty",
        //             image:'burger.png',
        //             price: '$10',
        //             numberadd:'7',
        //             numberremove:'8'      
        //         }
        //     ]
        // }
          
        }
    }
}
</script>

<style>

</style>