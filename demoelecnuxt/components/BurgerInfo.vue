<template>
    <div class="w-full"> 
        <h1 class="text-xl font-bold m-4">
            <!-- {{name}} -->
           {{burger.name}}
        </h1>
        <hr class="m-4 border-1 border-gray-400">
         <div class="flex justify-between ml-4 mr-4">
            <div>
                <h4 class="text-gray-600">Price</h4>
            </div>
            <div>
                <h4 class="text-gray-600">${{burger.price}}</h4>
            </div>          
        </div>
        <div class="flex justify-between ml-4 mr-4 mb-4" v-for="ingridient in ingridientInBurger" :key="ingridient.namee">
            <div>
                <h4 class="text-green-600" v-if="ingridient.count">{{ingridient.namee}}<span class="ml-4">x{{ingridient.count}}</span></h4>
                <!-- <h4 class="text-gray-600" v-if="ingridient.count">x{{ingridient.count}}</h4> -->
            </div>
            <!-- <div>
                <h4 class="text-gray-600" v-if="ingridient.count">x{{ingridient.count}}</h4>
            </div> -->
            <div>
                <h4 class="text-gray-600" v-if="ingridient.price">${{ingridient.price}}</h4>
            </div>          
        </div>
        <hr>
        <div class="flex justify-between ml-4 mr-4">
            <div>
                <h4 class="text-gray-600">Total Amount</h4>
            </div>
            <div>
                <h4 class="text-gray-600">${{totalPrice}}</h4>
            </div>          
        </div>
        <!-- <h4 class="text-md text-gray-600 p-4">Price:$10</h4> -->

    </div>
</template>

<script>
import BurgerIngDetails from '~/static/ingridients.json'
    function tempAlert(msg,duration){
        var el = document.createElement("div");
        el.setAttribute("style","position:absolute;bottom:0px;left:0px;background-color:red;color:white;height:40px;width:100%");
        el.classList.add("font-bold","text-center")
        el.innerHTML = msg;
        setTimeout(function(){
           el.parentNode.removeChild(el);
        },duration);
        document.body.appendChild(el);
}
export default {
    data(){
        return{
            ingridientInBurger:BurgerIngDetails.find((myBurger)=>this.burger.id == myBurger.id).ingridients,
            totalPrice:this.burger.price
        }
    },
    props:{
        burger:{
            type:Object,
            required:true
        }
    },
    // computed:{
    //      localIngredient(){
    //         BurgerIngDetails.find((myBurger)=>this.burger.id == myBurger.id).ingridients

    // //     } 

    // },
    mounted(){
        // console.log('mounted called')
        // this.$nuxt.refresh()
        this.$root.$on('add_content',(namee,price,count)=>{
            let array=this.ingridientInBurger
            console.log(array);
            if (array.find(arrayValue=>arrayValue.namee==namee)) {
                let index=array.findIndex(arrayValue=>arrayValue.namee==namee);
                // console.log(array[index].count);
                console.log(array[index]);
                array[index].price+=price
                array[index].count++
                this.totalPrice+=price
                //   console.log(window.location)
            } else {
                array.push({namee,price,count})
                this.totalPrice+=price
            }
        })
        this.$root.$on('remove_content',(namee,price,count)=>{
            let array=this.ingridientInBurger
            console.log(namee);
            if (this.ingridientInBurger.find(arrayValue=>arrayValue.namee==namee)) {
                let index=this.ingridientInBurger.findIndex(arrayValue=>arrayValue.namee==namee);
                if (array[index].count>1) {
                    array[index].count--
                    array[index].price-=price
                    this.totalPrice-=price
                }
                else{
                    array.splice(index,1)
                    // this.totalPrice-=price
                }

            } else {
            //    alert("Ingridient not added")
            tempAlert("Ingridient not added",2000) 
            }
        })
    },
    
}
</script>