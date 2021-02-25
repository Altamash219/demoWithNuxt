<template>
    <div class="w-full"> 
        <h1 class="text-xl font-bold m-4">
            <!-- {{name}} -->
           {{burger.name}}
        </h1>
        <hr class="m-4 border-1 border-gray-400">
        <div class="flex justify-between m-4">
                <h4 class="text-gray-600">Price</h4>
                <h4 class="text-gray-600">{{burger.price}}</h4>
        </div>
        <!-- <h4 class="text-md text-gray-600 p-4">Price:$10</h4> -->

    </div>
</template>

<script>
export default {
    data(){
        return{
            burger:{
                name:"Burger 1",
                price:"$10"
            }
        }
    }
    
}
</script>