<template>
    <div>
        <logo class="float-left h-16 w-16"/>
        <h1 class="text-center font-serif text-bold text-2xl">Scan QR code And Pay</h1>
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
            QrImage:'qr.png'
        }
    },
    mounted(){
        var connect = new WebSocket("ws://localhost:8000")
         setTimeout(() => {
            this.QrImage = 'success.jpeg'
            connect.onopen=function (event) {
            console.log(event);
            console.log("Successfully connected to websocket");
            // connect.send("From javascript")
            }
        }, 5000);
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