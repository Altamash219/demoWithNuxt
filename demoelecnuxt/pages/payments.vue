<template>
    <div>
        <h1 class="text-center font-serif text-bold text-2xl">Scan QR code And Pay</h1>
        <img :src="require(`~/assets/${QrImage}`)" class="rounded-xl qr m-auto">
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
.qr{
    width: 70vh;
    height: 70vh;
}
</style>