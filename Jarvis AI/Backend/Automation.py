from AppOpener import close,open as appopen
from webbrowser import open as webopen
from pywhatkit import search,playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import keyboard 
import asyncio
import os 

# Load environment variables from the .env file
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

#Define CSS classes for parsing specefic elements in HTML content 
classes = ["zCubwf", "hgKElc", "LTKOO SY7ric", "ZOLcW", "gsrt vk_bk FzvWSb YwPhnf", 
           "pclqee", "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "05uR6d LTKOO", "vlzY6d",
           "webanswers-webanswers_table_webanswers-table", "dDoNo ikb4Bb gsrt", 
           "sXLa0e", "LWkfKe", "VQF4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]

#Define a user-agent for making web requests
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

#Initialize the Groq client with the API key
client = Groq(api_key=GroqAPIKey)

#Predefined professional responses for user interactions.
professional_responses = [
    "Your satisfaction is my priority. How can I assist you further?",
    "I'm at your service. What else can I do for you?",
]

#List to store chatbot messages 
messages = []
#System message to provide context to the chatbot.
SystemChatBot=[{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like letters, codes, applications, essays, notes, songs, poems etc."}]
#Function to perform aa google search 
def GoogleSearch(Topic):
    search(Topic)
    return True


#Function to generate content using AI and save it to a file 
# Define or import client, SystemChatBot, and messages elsewhere before using this function

def Content(Topic):
    # Ensure Data folder exists
    os.makedirs("Data", exist_ok=True)

    # Nested function to open a file in notepad
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    # Nested Function to generate content using AI chatbot
    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f'{prompt}'})
        
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer

    Topic = Topic.replace("Content", "")
    ContentByAI = ContentWriterAI(Topic)

    file_path = rf"Data\{Topic.lower()}.txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(ContentByAI)

    OpenNotepad(file_path)
    return True

# Example usage
#Content("application for sick leave")

def YouTubeSearch(Topic):
    Url4Search=f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

#Function to play a video on YouTube
def PlayYouTube(query):
    playonyt(query)
    return True

#PlayYouTube("Dhun")

#Function to open an application or a relevant webpage 
def OpenApp(app,sess=requests.session()):
    try:
        appopen(app, match_closest=True,output=True, throw_error=True)
        return True
    except:
        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', {'jsname':'UWckNb'})
            return [link.get('href')for link in links]
        
        # Nested function to perform a Google search and retrieve HTML.
        def search_google(query):
            url = f"https://www.google.com/search?q={query}"
            headers = {"User-Agent": useragent} # Use the predefined use
            response = sess.get(url, headers=headers) # Perform the GET

            if response.status_code == 200:
                return response.text # Return the HTML content.
            else:
                print("Failed to retrieve search results.") # Print an e
            return None
        html = search_google(app)# Perform the Google search.
        if html:
            link=extract_links(html)[0]
            webopen(link)
        return True

#Function to close an application.
def CloseApp(app):
    if "chrome" in app:
        pass 
    else:
        try:
            close(app, match_closest= True, output= True, throw_error= True) 
            return True 
        except:
            return False
        
#Function to execute system-level comsands.
def System(command):
    def mute():
        keyboard.press_and_release("volume mute")
#Nested function to unmure the systém volume.
    def unmute():
        keyboard.press_and_release("volumemute")
#Nested function to increase the system volume.
    def volume_up():
        keyboard.press_and_release("volume up")
    def volume_down():
        keyboard.press_and_release("volume down")
    #Execute the appropriate connaitd.
    if command =="mute":
        mute()
    elif command== "unmute":
        unmute()
    elif command=="volume up": 
        volume_up()
    elif command== "volume down":
        volume_down()
    return True

#Asynchronous function to translate and execute user commands.
async def TranslateAndExecute(commands:list[str]):
    Funcs=[]#List to store asynchronous tasks,
    for command in commands:
        if command.startswith("open "):
            if "open it" in command:
                pass
            if "open file"== command:
                pass
            else:
                fun= asyncio.to_thread(OpenApp, command.removeprefix("open"))
                Funcs.append(fun)

        elif command.startswith("general"):
            pass
        elif command.startswith("realtime "):
            pass
        elif command.startswith("close"):
            fun=asyncio.to_thread(CloseApp, command.removeprefix("close"))
            Funcs.append(fun)

        elif command.startswith("play"):
            fun= asyncio.to_thread (PlayYouTube, command.removeprefix ("play "))
            Funcs.append(fun)
        elif command.startswith("content"): 
            fun= asyncio.to_thread(Content, command.removeprefix("content"))
            Funcs.append(fun)
        
        elif command.startswith("google search "):
            fun= asyncio.to_thread(GoogleSearch, command.removeprefix("google search"))
            Funcs.append(fun)

        elif command.startswith("youtube search"):
            fun=asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search")) 
            Funcs.append(fun)
        
        elif command.startswith("system"):
            fun= asyncio.to_thread(System, command.removeprefix("system"))
            Funcs.append(fun)
        else:
            print(f"No Function Found. For {command}")
    results=await asyncio.gather(*Funcs)

    for result in results:
        if isinstance(result, str):
            yield result
        else:
            yield result

#Asynchronous function to automate command execution.
async def Automation (commands: list[str]):
    async for result in TranslateAndExecute(commands): 
        pass
    return True  
