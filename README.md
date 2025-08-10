# Jarvix – AI Assistant

**Jarvix is an intelligent AI assistant built with Python that can think, listen, speak, and perform multiple tasks — 
including real-time Q&A, PC automation, AI image generation, content creation, and multilingual support.**

## Features

* Voice & Text Input – Accepts commands via microphone or text

* Smart Chatbot – AI-powered conversation using Cohere API

* Real-Time Search – Fetches and summarizes live web data with Groq API

* PC Automation – Opens/controls apps and system settings

* AI Image Generation – Creates high-quality images via HuggingFace API

* Text-to-Speech – Natural voice output using Edge-TTS

* Persistent Storage – Saves chat logs, generated images, and documents

## Tech Stack

* Language:

   * Python 3.10+

* Libraries & Frameworks:

   * PyQt5 – GUI

   * Selenium – Browser automation

   * Pygame – Audio handling

   * Pillow – Image processing

   * Requests / BeautifulSoup – Web scraping

   * Edge-TTS – Speech synthesis

   * mtranslate – Translation

* APIs:

   * Cohere – NLP & decision-making

   * Groq – Real-time summarization

   * HuggingFace – AI image generation

* Tools:

   * ChromeDriver – Selenium support

   * python-dotenv – Secure environment variable handling

## Project Structure

Jarvix/Jarvis AI

│

├── Backend/

|  ├── Model.py                # Decision-making logic

|  ├── Chatbot.py              # AI chatbot using Cohere API

|  ├── RealtimeSearchEngine.py # Real-time search + Groq summarization

|  ├── Automation.py           # PC and system task automation

|  ├── ImageGeneration.py      # AI image generation

|  ├── SpeechToText.py         # Voice input to text

|  ├── TextToSpeech.py         # Text-to-speech output

|

├── Data/ # Stores chat logs, images, docs, audio

|

├── Frontend/

|  ├── .gitignore

|  ├── Main.py                 # Entry point, integrates all modules

|  ├── Requirements.txt        # Dependencies list

├── LICENSE

│

└── README.md

## Installation

1️. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/Jarvix.git
    cd Jarvix

2️. **Install dependencies**

    ```bash
    pip install -r Requirements.txt
    
3️. **Set up environment variables**

   * Create a .env file in the project root

   * Add your API keys:
     
     * COHERE_API_KEY=your_key_here
       
     * GROQ_API_KEY=your_key_here
       
     * HF_API_KEY=your_key_here
    
4️. **Run the application**

    ```bash
    python Main.py
    
## System Architecture

(Make sure to replace architecture.png with your actual diagram file)

## Screenshots

* GUI
* 
<img width="1280" height="723" alt="image" src="https://github.com/user-attachments/assets/7cb8f21e-a175-4099-b53b-11ed32eb4b3f" />

* ChatBot

  <img width="1280" height="719" alt="image" src="https://github.com/user-attachments/assets/c39341e3-dccb-4bd6-b27e-707b93b3834f" />
  
  <img width="1280" height="719" alt="image" src="https://github.com/user-attachments/assets/72d0b1f8-158b-4ecc-be7c-c126a9491c4d" />

* Image Generation Output

  <img width="1600" height="851" alt="image" src="https://github.com/user-attachments/assets/8e33b762-f495-46fe-bdce-5f9bce682fce" />
 
  <img width="1600" height="852" alt="image" src="https://github.com/user-attachments/assets/3ebfd99e-e4bf-472f-9594-2f75e6ef1e11" />

  <img width="1600" height="843" alt="image" src="https://github.com/user-attachments/assets/68872e95-31b8-476e-88f1-4a9ecb4737ca" />

* Speech to text

  <img width="1280" height="719" alt="image" src="https://github.com/user-attachments/assets/6dac37cd-a526-414e-a260-e953b0ee8946" />

  <img width="1147" height="694" alt="image" src="https://github.com/user-attachments/assets/b5aceb54-4f98-403d-a487-67733818a17e" />


## How It Works

* User provides voice or text input

* Input goes to SpeechToText (if voice)

* Model.py decides whether it’s a chatbot, search, automation, or image request

* Executes task through the respective module

* TextToSpeech + GUI present results

* All data saved to Data folder

## Future Enhancements

* Internet of Things (IoT) device control

* Advanced behavioral learning or emotional intelligence

* Offline LLM support

* Multi-user profiles

* Calendar & email automation

* Mobile deployment

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## License

This project is licensed under the [MIT License](LICENSE).
