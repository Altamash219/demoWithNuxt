<template>
    <div>
        <h1 class="text-center font-serif text-bold text-2xl">Scan QR code And Pay</h1>
        <img :src="require(`~/assets/${QrImage}`)" class="rounded-xl qr m-auto">
        <primary-button action="Back" class="btnn w-56 ml-4" topage="/menu" id="21"></primary-button>
        <number-for-component number="22" class="float-left mt-5 ml-60"/>
    </div>
</template>
<script>
export default {
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