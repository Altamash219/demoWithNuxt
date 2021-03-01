import speech_recognition as sr
import asyncio
import websockets

# Configuring websocket connection and sending message over the websocket to the server


async def hello(text):
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
# Analyzing user input to send command to the server accordingly


def anaylzeTask(command):
    # print(command.split(' ')[1])
    print(command)
    commandList = command.split(' ')

    # commandToCheck = command.split(' ')[1]
    #action = command
    # commandList[0] = command.split(' ')[0]
    if(commandList[1] == "1") or (commandList[1] == "one") or (commandList[1] == "bun"):
        return "1"
    elif(commandList[1] == "2") or (commandList[1] == "to") or (commandList[1] == "two"):
        return "2"
    elif(commandList[1] == "3") or (commandList[1] == "tree") or (commandList[1] == "three"):
        return "3"
    elif(commandList[1] == "4") or (commandList[1] == "four"):
        return "4"
    elif(keyword=="add") or (keyword == "ad") or (keyword == "at"):
        if(commandToCheck=="cheese") or (commandToCheck=="chains") or (commandToCheck=="chain"):
            return "11"
        elif(commandToCheck=="patti") or (commandToCheck=="peti") or (commandToCheck=="patty") or (commandToCheck=="fati"):
            return "17"
        elif(commandList[1] == "tomato"):
            return "13"
        elif(commandList[1] == "onion"):
            return "15"
        else:
            return "First"
    elif(commandList[0] == "remove"):
        if(commandList[1] == "cheese") or (commandList[1] == "chains") or (commandList[1] == "chain"):
            return "12"
        elif(commandToCheck=="patti") or (commandToCheck=="peti") or (commandToCheck=="patty") or (commandToCheck=="fati"):
            return "18"
        elif(commandList[1] == "tomato"):
            return "14"
        elif(commandList[1] == "onion"):
            return "16"
        else:
            return "Second"
    elif(commandList[0] == "confirm"):
        print("Said continue")
        return "20"
    elif(commandList[0] == "back"):
        print("Said back")
        return "21"
    else:
        return "Third"

# Recording user audio and converting it to text


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:                         # get input from mic
        print("Listening")
        voice = recognizer.record(source, duration=4)
        try:
            command = recognizer.recognize_google(
                voice).lower()  # use google API
            # all words lowercase- so that we can process easily
            #command = command.lower()
            # look for wake up word in the beginning
            print(command)
            if(command == "place an order"):
                return "99"
            elif(command == "confirm"):
                return "20"
            elif(command == "back"):
                return "21"
            else:
                commandAnalyzed = anaylzeTask(command)
                return commandAnalyzed
        except:
            return "Forth"


    # if (command.split(' ')[0] == "casper") or (command.split(' ')[0]=="kasper"):
        # 			# if wake up word found....
    #   print("[wake-up word found]")
    #   return command
if __name__ == "__main__":
    while(True):
        text = listen()
        asyncio.get_event_loop().run_until_complete(hello(text))
