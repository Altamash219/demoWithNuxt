import speech_recognition as sr
import asyncio
import websockets
#Configuring websocket connection and sending message over the websocket to the server
async def hello(text):
    uri="ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
#Analyzing user input to send command to the server accordingly
def anaylzeTask(command):
    print(command.split(' ')[1])
    commandToCheck=command.split(' ')[1]
    action=command
    keyword=command.split(' ')[0]
    if(commandToCheck=="1") or (commandToCheck=="one") or (commandToCheck=="bun"):
        return "1"
    elif(commandToCheck=="2") or (commandToCheck=="to") or (commandToCheck=="two"):
        return "2"
    elif(commandToCheck=="3") or (commandToCheck=="tree") or (commandToCheck=="three"):
        return "3"
    elif(commandToCheck=="4") or (commandToCheck=="four"):
        return "4"
    elif(keyword=="add") or (keyword == "ad") or (keyword == "at"):
        if(commandToCheck=="cheese") or (commandToCheck=="chains") or (commandToCheck=="chain"):
            return "11"
        elif(commandToCheck=="patti") or (commandToCheck=="peti") or (commandToCheck=="patty") or (commandToCheck=="fati"):
            return "17"
        elif(commandToCheck=="tomato"):
            return "13"
        elif(commandToCheck=="onion"):
            return "15"
        else:
            return "Please Speak Again"
    elif(keyword=="remove"):
        if(commandToCheck=="cheese") or (commandToCheck=="chains") or (commandToCheck=="chain"):
            return "12"
        elif(commandToCheck=="patti") or (commandToCheck=="peti") or (commandToCheck=="patty") or (commandToCheck=="fati"):
            return "18"
        elif(commandToCheck=="tomato"):
            return "14"
        elif(commandToCheck=="onion"):
            return "16"
        else:
            return "Please Speak Again"
    elif(action=="continue"):
        print("Said continue")
        return "20"
    elif(action=="back"):
        print("Said back")
        return "21"
    else:
        return "Please Speak Again"

#Recording user audio and converting it to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:                         # get input from mic
        print("Listening")
        voice = recognizer.record(source,duration=4) 
        try:
            command = recognizer.recognize_google(voice).lower()  # use google API
			# all words lowercase- so that we can process easily
			#command = command.lower()
			# look for wake up word in the beginning
            print(command)
            commandAnalyzed=anaylzeTask(command)
            print(commandAnalyzed)
            return commandAnalyzed
        except:
            return "Please Speak Again"

    # if (command.split(' ')[0] == "casper") or (command.split(' ')[0]=="kasper"):
	# 			# if wake up word found....
    #   print("[wake-up word found]")
    #   return command
if __name__ == "__main__":
    while(True):
        text=listen()
        asyncio.get_event_loop().run_until_complete(hello(text))