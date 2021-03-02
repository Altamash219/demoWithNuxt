<template>
    <div>
        <logo class="float-left h-16 w-16"/>
        <h1 class="text-center font-serif text-bold text-2xl">{{text}}</h1>
        <img :src="require(`~/assets/${QrImage}`)" class="rounded-xl qr m-auto">
        <primary-button action="Back" class="btnn w-56 ml-4" topage="/menu" id="21"></primary-button>
        <number-for-component number="22" class="float-left mt-5 ml-60"/>
    </div>
</template>
<script>
import Logo from "~/components/Logo";
export default {
    components:{
        Logo,
    },
    data(){
        return{
            QrImage:'qr.png',
            text:'Scan QR code and pay'
        }
    },
    mounted(){
        
    setTimeout(() => {
        // var connect = new WebSocket("ws://localhost:8000")
        this.QrImage = 'success.jpeg'
        this.text='PayMent Successful!! Your Order no. is 40'
        // this.$root.$on("websocket",(connect)=>{
        //     connect.onopen=function (event) {
        //     // console.log(event);
        //     // console.log("Websocket connected");
        //     // console.log("Successfully connected to websocket");
        //     connect.send("Payment Successful")
        // }
        // })
        
    }, 5000);
        // connect.onmessage=function (event) {
        //     actionMessage=event.data
        //     // console.log(window.location);
        //     if (actionMessage!="Please Speak Again") {
        //         const el = document.getElementById(`${actionMessage}`)
        //     if(el){
        //         el.firstChild.click()
        //     }else{
        //         console.log('Invalid Option')
        //         // alert("invalid")
        //         tempAlert("Invalid option",2000)
        //     }
        //     }

            
        //     console.log("Message from server:",actionMessage);
        // }
       
    }
}
</script>
<style>
.btnn{
    height: 50px;
    background-color: green;
    margin-top: 40px;
    margin-right: 40px;
}
.qr{
    width: 70vh;
    height: 70vh;
}
</style>