<template>
    <div class="flex-grow h-screen my-auto">
        <ul class="bg-white">
            <li v-for="ingridientt in ingridient" :key="ingridientt.name" class="m-4 border-2 border-white shadow-lg rounded-2xl">
                <div class="flex">
                    <primary-button action="+" class="w-16 text-xl text-center m-4"/>
                    <h4 class="m-4 m-auto font-bold text-lg uppercase">{{ingridientt.name}}</h4>
                    <primary-button action="-" class="w-16 text-xl text-center m-4"/>
                </div>
            </li>
        </ul>
        <primary-button action="Confirm Order And Pay" class="btnn w-56" topage="/payments"></primary-button>
    </div>
</template>

<script>
import PrimaryButton from '~/components/PrimaryButton'
export default {
    props:{
        ingridient:{
            type:Array,
            required:true
        }
    },
    components:{
        PrimaryButton,
    }
}
</script>
<style scoped>
.btnn{
    height: 50px;
    background-color: green;
    float: right;
    margin-top: 40px;
    margin-right: 40px;
}
</style>
