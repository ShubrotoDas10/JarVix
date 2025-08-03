from googlesearch import search
from groq import Groq
from json import load,dump
import datetime
from dotenv import dotenv_values

#load environment variables from the .env file
env_vars = dotenv_values(".env")

#Retrieve environment variables for the chatbot configuration
Username = env_vars.get("Username")
AssistantName = env_vars.get("AssistantName")
GroqAPIKey = env_vars.get("GroqAPIKey")

#Initialize Groq client with the API key
client = Groq(api_key=GroqAPIKey)

#Define the system instructions for the chatbot

System= f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {AssistantName} which has real-time up-to-date information from the internet.
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Just answer the question from the provided data in a professional way. ***"""

#tryto load the chat from a JSON file , or create an empty one if it doesn't exist.
try:
    with open("Data\ChatLog.json", "r") as f:
        message = load(f)
except :
    with open("Data\ChatLog.json", "w") as f:
        dump([], f)

#Function to search the web using Google Search and format results
def GoogleSearch(query):
    results = list(search(query, advanced=True,num_results=5))
    Answer = f"The search results for '{query}' are:\n[start]\n"
    for i in results:
        Answer += f"Title:{i.title}\nDescription:{i.description}\n\n"
    Answer += "[end]"
    return Answer
    
#Function to cleanup the answer by removing empty lines.
def AnswerModifier(Answer):
    lines = Answer.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = "\n".join(non_empty_lines)
    return modified_answer

#Predefined chatbot conversation system message and an initial user message 

SystemChatBot = [
    {"role": "system", "content": System},
    {"role": "user", "content": "hi",},
    {"role": "assistant", "content": "Hello, how can I help you ?"}
]

#Function to get reael-time information like the current date and time
def Information():
    data =""
    current_data_time= datetime.datetime.now()
    day=current_data_time.strftime("%A")
    date=current_data_time.strftime("%d")
    month=current_data_time.strftime("%B")
    year=current_data_time.strftime("%Y")
    hour=current_data_time.strftime("%H")
    minute=current_data_time.strftime("%M")
    second=current_data_time.strftime("%S")
    data += f"Use This Real-time Information if needed :\n"
    data += f"Day: {day}\n"
    data += f"Date: {date}\n"
    data += f"Month: {month}\n"
    data += f"Year: {year}\n"
    data += f"Time: {hour} hours, {minute} minutes, {second}seconds.\n"

    return data

#Function to handle real-time search and response generation.
# Function to handle real-time search and response generation.
def RealtimeSearchEngine(prompt):
    global SystemChatBot, message

    # Load the chat log from the JSON file
    with open("Data\\ChatLog.json", "r") as f:
        message = load(f)
    message.append({"role": "user", "content": f"{prompt}"})

    # Add Google Search results to the system chatbot messages.
    SystemChatBot.append({"role": "system", "content": GoogleSearch(prompt)})

    # Generate a response using the Groq client 
    compltion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=SystemChatBot + [{"role": "system", "content": Information()}] + message,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stream=True,
        stop=None
    )

    Answer = ""

    # Concatenate the response chunks from the streaming output
    for chunk in compltion:
        if chunk.choices[0].delta.content:
            Answer += chunk.choices[0].delta.content

    # Clean up the response.
    Answer = Answer.strip().replace("</s>", "")
    message.append({"role": "assistant", "content": Answer})

    # Save the updated chat log to the JSON file
    with open("Data\\ChatLog.json", "w") as f:
        dump(message, f, indent=4)

    # Remove the most recent system message from the chatbot conversation.
    SystemChatBot.pop()

    return AnswerModifier(Answer=Answer)
    #Main entry point of the program for interactive querying
if __name__ == "__main__":
    while True:
        prompt = input("Enter your query:")
        print(RealtimeSearchEngine(prompt))
         
