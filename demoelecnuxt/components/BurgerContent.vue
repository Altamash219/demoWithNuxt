<template>
    <div class="flex-grow h-screen">
        <ul class="bg-white">
            <li v-for="ingridientt in ingridient" :key="ingridientt.name" class="m-4 mb-20 border-2 border-white shadow-lg rounded-2xl">
                <div class="flex">
                    <number-for-component :numberadd="ingridientt.numberadd"/>
                    <primary-button action="+" @click="addIngridient(ingridientt.name,ingridientt.price,1, burgerId)" :id="ingridientt.numberadd" class="w-16 text-xl text-center m-4"/>
                    <h4 class="m-4 m-auto font-bold text-lg uppercase">{{ingridientt.name}}</h4>
                    <primary-button action="-" @click="removeIngridient(ingridientt.name,ingridientt.price,1, burgerId)" :id="ingridientt.numberremove" class="w-16 text-xl text-center m-4"/>
                    <number-for-component :numberremove="ingridientt.numberremove"/>
                </div>
            </li>
        </ul>
        <primary-button action="Confirm Order And Pay" class="btnn w-56 float-right" topage="/payments" id="20"></primary-button>
        <number-for-component number=20 numberText="twenty" class="float-right mt-5" />
        <primary-button action="Back" class="btnn w-56 float-left ml-4" topage="/" id="21"></primary-button>
        <number-for-component number=21 numberText="twentyone" class="float-left mt-5"/>
    </div>
</template>

<script>
import NumberForComponent from '~/components/NumberForComponent'
import PrimaryButton from '~/components/PrimaryButton'
export default {
    props:{
        ingridient:{
            type:Array,
            required:true
        },
        burgerId:{
            type: Number,
            required : true
        }
    },
    components:{
        PrimaryButton,
        NumberForComponent
    },
    methods:{
        addIngridient:function(namee,price,count, burgerId){
            this.$root.$emit("add_content",namee,price,count, burgerId)
        },
        removeIngridient:function(namee,price,count, burgerId) {
            this.$root.$emit("remove_content",namee,price,count, burgerId)
        }
        // addIngridient(name){
        //     console.log(name);
        // }
    }
}
</script>
<style scoped>
.btnn{
    height: 50px;
    background-color: green;
    margin-top: 40px;
    margin-right: 40px;
}
</style>
