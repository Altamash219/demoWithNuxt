<template>
    <div>
        <h1 class="text-center font-serif text-bold text-2xl">Scan QR code And Pay</h1>
        <img :src="require(`~/assets/${QrImage}`)" class="rounded-xl qr m-auto">
        <primary-button action="Back" class="btnn w-56 ml-4" topage="/" id="twentytwo"></primary-button>
        <number-for-component number="22" class="float-left mt-5 ml-60"/>
    </div>
</template>
<script>
export default {
    data(){
        return{
            QrImage:'qr.png'
        }
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