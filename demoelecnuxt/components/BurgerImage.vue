<template>
    <div class="flex overflow-hidden border-white border-2 rounded-2xl shadow-xl">
        <img :src="require(`~/assets/${order.image}`)" class="rounded-xl max-w-md">
        <burger-info class="p-5" :burger="order" />
    </div>
</template>
<script>
import PrimaryButton from '~/components/PrimaryButton';
import BurgerInfo from '~/components/BurgerInfo';
export default {
    components:{
        PrimaryButton,
        BurgerInfo
    },
   props:{
       order:{
           type:Object,
           required:true
       }
   }
}
</script>
<style>
/* .order{
    display : flex;
    flex-direction: column;
    width:400px;
} */
</style>