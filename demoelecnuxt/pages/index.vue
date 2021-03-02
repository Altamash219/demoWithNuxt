<template>
  <div class="container">
    <logo/>
  </div>
</template>

<script>
import Logo from '~/components/Logo';
function tempAlert(msg,duration){
    var el = document.createElement("div");
    el.setAttribute("style","position:absolute;bottom:0px;left:0px;background-color:red;color:white;height:40px;width:100%");
    el.classList.add("font-bold","text-center")
    el.innerHTML = msg;
    setTimeout(function(){
       el.parentNode.removeChild(el);
    },duration);
    document.body.appendChild(el);
}
export default {
  components:{Logo},
  mounted(){
        var connect = new WebSocket("ws://localhost:8000")
    //    var connect = new WebSocket("ws://localhost:8000")
    //     var actionMessage;
    //     // (connect)=>{
    //     //     this.$root.$emit("websocket",connect)
    //     // }
    //     connect.onmessage=function (event) {
    //         actionMessage=event.data
    //         // console.log(window.location);
    //         if (actionMessage!="Please Speak Again") {
    //             const el = document.getElementById(`${actionMessage}`)
    //         if(el){
    //             el.firstChild.click()
    //         }else{
    //             console.log('Invalid Option')
    //             // alert("invalid")
    //             tempAlert("Invalid option",2000)
    //         }
    //         }

            
    //         console.log("Message from server:",actionMessage);
    //     }
    //    connect.onopen=function (event) {
    //         console.log(event);
    //         console.log("Successfully connected to websocket");
    //         // connect.send("From javascript")
    //     } 
    // }
    var actionMessage;
        connect.onmessage=function (event) {
            actionMessage=event.data
            // console.log(window.location);
            if (actionMessage!="Please Speak Again" && actionMessage!="Payment Successful") {
                const el = document.getElementById(`${actionMessage}`)
            if(el){
                el.firstChild.click()
            }else{
                console.log('Invalid Option')
                // alert("invalid")
                tempAlert("Invalid option",2000)
            }
            }

            
            console.log("Message from server:",actionMessage);
        }
       connect.onopen=function (event) {
            console.log(event);
            console.log("Successfully connected to websocket");
            //connect.send("From javascript")
        }
   
}
  
}
</script>

<style>
/* Sample `apply` at-rules with Tailwind CSS
.container {
@apply min-h-screen flex justify-center items-center text-center mx-auto;
}
*/
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
