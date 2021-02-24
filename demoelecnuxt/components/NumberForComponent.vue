<template>
<div>
    <h6 class="text-gray-600" v-if="number">({{number}})</h6>
    <h6 class="text-gray-600" v-if="numberadd">({{numberadd}})</h6>
    <h6 class="text-gray-600" v-if="numberremove">({{numberremove}})</h6>
</div>
    
</template>
<script>
export default {
    props:{
        number:{
            type:String,
            default:""
        },
        numberadd:{
            type:String,
            default:""
        },
        numberremove:{
            type:String,
            default:""
        }
    }
}
</script>