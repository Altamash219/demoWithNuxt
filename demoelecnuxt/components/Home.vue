<template>
<div>
    <div>
        <logo class="float-left h-16 w-16"/>
        <h1 class="text-3xl font-bold text-center uppercase m-24">Select Your Burger</h1>

    </div>
    <div class="container">
        <div v-for="food in foods" :key="food.name">
            <FoodCard :food="food"/>
        </div>
    </div>
</div>
</template>

<script>
import FoodCard from '~/components/FoodCard';
import Foods from '~/static/foods.json'
import Logo from './Logo.vue';
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
    components:{
        FoodCard,
        Logo
    },
    mounted()
    {
        // var connect = new WebSocket("ws://localhost:8000")
        this.$root.$on("websocket",(connect)=>{
            var actionMessage;
        connect.onmessage=function (event) {
            actionMessage=event.data
            // console.log(window.location);
            if (actionMessage!="Please Speak Again" && actionMessage!="Payment Successful") {
                const el = document.getElementById(`${actionMessage}`)
            if(el){
                el.firstChild.click()
            }else{
                console.log('Invalid Option')
                // alert("invalid")
                tempAlert("Invalid option",2000)
            }
            }

            
            console.log("Message from server:",actionMessage);
        }
       connect.onopen=function (event) {
            console.log(event);
            console.log("Successfully connected to websocket");
            connect.send("From javascript")
        }
        })
    },
    data(){
        return{
            foods:Foods,

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
