<template>
  <div class="card">
    <div
      class="card-image"
      :style="{
        backgroundImage:
          'url(' + require(`~/assets/${food.image}`) + ')',
      }"
    ></div>
    <div class="card-content">
      <h3 class="font-bold text-2xl text-gray-900 mb-1">{{ food.name }}</h3>
      <p class="text-md text-gray-600">
        {{ food.price }}
      </p>
      <primary-button action="Add to Cart" topage="/placeorders" class="mt-8"/>
      <number-for-component :number="food.number"/>
    </div>
  </div>
</template>

<script>
import NumberForComponent from '~/components/NumberForComponent'
import PrimaryButton from '~/components/PrimaryButton'
export default {
  components:{
    PrimaryButton,
    NumberForComponent
  },
  props: {
    food: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.card{
  border: 2px solid #ffffff;
  border-radius: 15px;
  -webkit-box-shadow: 0 6px 6px -6px #000;
  -moz-box-shadow: 0 5px 6px -6px #000;
  box-shadow: 0 5px 6px -6px #000;
  margin: 20px;
  min-width: 20rem;
  height: 25rem;
  max-width: 30rem;
  overflow: hidden;
}
.card-image{
  height: 14rem;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  /* background-image: url('../assets/burger.png'); */
}

.card-content{
  text-align: center;
  padding:16px;
  /* background: rgba(209, 213, 219, 1); */
}


</style>
