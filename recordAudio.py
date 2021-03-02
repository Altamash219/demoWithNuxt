import speech_recognition as sr
import asyncio
import time
import websockets
import pyttsx3
# import gTTS
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
    if(commandList[0] == "aloo") or (commandList[0] == "aaloo") or (commandList[0] == "one") or (commandList[0] == "1"):
        return "1"
    elif(commandList[0] == "maharaja") or (commandList[0] == "to") or (commandList[0] == "two") or (commandList[0] == "2"):
        return "2"
    elif(commandList[0] == "cheese") or (commandList[0] == "cheeseburger") or (commandList[1] == "three") or (commandList[0] == "3"):
        return "3"
    elif(commandList[0] == "double") or (commandList[0] == "4") or (commandList[0] == "four") or (commandList[0] == "for"):
        return "4"
    elif(commandList[0]
         == "add") or (commandList[0]
                       == "ad") or (commandList[0]
                                    == "at"):
        if(commandList[1]
           == "cheese") or (commandList[1]
                            == "chains") or (commandList[1]
                                             == "chain"):
            return "11"
        elif(commandList[1]
             == "patti") or (commandList[1]
                             == "peti") or (commandList[1]
                                            == "patty") or (commandList[1]
                                                            == "fati"):
            return "17"
        elif(commandList[1] == "tomato"):
            return "13"
        elif(commandList[1] == "onion"):
            return "15"
        else:
            return "Can You Repeat"
    elif(commandList[0] == "remove"):
        if(commandList[1] == "cheese") or (commandList[1] == "chains") or (commandList[1] == "chain"):
            return "12"
        elif(commandList[1]
             == "patti") or (commandList[1]
                             == "peti") or (commandList[1]
                                            == "patty") or (commandList[1]
                                                            == "fati"):
            return "18"
        elif(commandList[1] == "tomato"):
            return "14"
        elif(commandList[1] == "onion"):
            return "16"
        else:
            return "Can you repeat"
    elif(commandList[0] == "confirm"):
        print("Said continue")
        return "20"
    elif(commandList[0] == "back"):
        print("Said back")
        return "21"
    else:
        return "Please Speak Again"


def speak(audio):
    time.sleep(5)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

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
                #speak("Payment Successful")
                return "20"
            elif(command == "back"):
                return "21"
            else:
                commandAnalyzed = anaylzeTask(command)
                return commandAnalyzed
        except:
            return "Please Speak Again"


if __name__ == "__main__":
    while(True):
        text = listen()
        audio = asyncio.get_event_loop().run_until_complete(hello(text))
    # speak("payment successful")
