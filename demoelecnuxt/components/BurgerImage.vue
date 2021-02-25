<template>
    <div class="flex overflow-hidden border-white border-2 rounded-2xl shadow-xl">
        <img :src="require(`~/assets/${orderImage}`)" class="rounded-xl">
        <burger-info class="p-5"/>
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
       orderImage:{
           type:String,
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