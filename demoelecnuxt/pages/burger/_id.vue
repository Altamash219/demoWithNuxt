<template>
    <div>
        <PlaceOrder/>
    </div>
</template>
<script>
import PlaceOrder from '~/components/PlaceOrder'
export default {
    components:{
        PlaceOrder
    },
    validate({params}){
        if(params.id){
            return true
        }
    }
}
</script>