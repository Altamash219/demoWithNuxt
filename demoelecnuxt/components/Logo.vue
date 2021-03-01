<template>
    <div id="99">
        <nuxt-link to="/menu">
        <img :src="require(`assets/PNTLogo.jpeg`)" alt="logo">
        </nuxt-link>
    </div>
</template>

<script>
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
    mounted(){
       var connect = new WebSocket("ws://localhost:8000")
        var actionMessage;
        (connect)=>{
            this.$root.$emit("websocket",connect)
        }
        connect.onmessage=function (event) {
            actionMessage=event.data
            // console.log(window.location);
            if (actionMessage!="Please Speak Again") {
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
            // connect.send("From javascript")
        } 
    }
   
}
</script>