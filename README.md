# Alexa Voice Assistant Clone

This project is a Python-based voice assistant that mimics some functionalities of Amazon's Alexa. The assistant can play songs on YouTube, tell the current time, give brief summaries from Wikipedia, tell jokes, open Notepad, perform Google searches, and more based on voice commands.

## How It Works

The voice assistant listens for commands and performs actions accordingly. It can:
- Play songs on YouTube
- Tell the current time
- Provide summaries from Wikipedia
- Tell jokes
- Open Notepad
- Perform Google searches
- Provide information about various topics
- Respond to specific conversational prompts

## Getting Started

To run this project on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- Install the required libraries using the following command:

``bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes psutil googlesearch-python

## Running the Voice Assistant
1. Clone the repository:

``bash
git clone https://github.com/yourusername/alexa-voice-assistant-clone.git
cd alexa-voice-assistant-clone

2. Run the Python file:
``bash
python alexa_voice_assistant.py

3. The assistant will start listening for commands. Use the keyword "Alexa" followed by your command. For example:

 - "Alexa, play Despacito on YouTube"
 - "Alexa, what is the time?"
 - "Alexa, who is Albert Einstein?"
 - "Alexa, tell me a joke"
 - "Alexa, open Notepad"
 - "Alexa, search for Python tutorials on Google"

## Commands

 - Play a song on YouTube: Say "Alexa, play [song name]"
 - Tell the current time: Say "Alexa, what is the time?"
 - Get a summary from Wikipedia: Say "Alexa, who is [person name]" or "Alexa, tell me about [topic]"
 - Tell a joke: Say "Alexa, tell me a joke"
 - Open Notepad: Say "Alexa, open Notepad" or "Alexa, open editor"
 - Perform a Google search: Say "Alexa, search for [query]" or "Alexa, Google [query]"
 - Exit the assistant: Say "Alexa, exit" or "Alexa, stop"

 ## Code Overview

The main functionalities are implemented in the alexa_voice_assistant.py file:

### Libraries Imported:

 - speech_recognition for recognizing speech input.
 - pyttsx3 for text-to-speech conversion.
 - pywhatkit for playing YouTube videos.
 - datetime for fetching current time.
 - wikipedia for fetching summaries from Wikipedia.
 - pyjokes for fetching jokes.
 - subprocess for opening applications like Notepad.
 - webbrowser for performing web searches.
 - psutil for monitoring processes.
 - googlesearch for performing Google searches.

 ### Functions:

 - talk(text): Converts text to speech.
 - take_command(): Listens for voice commands.
 - run_alexa(): Processes the voice commands and performs corresponding actions.

### Main Loop:

 - Continuously listens for commands and processes them.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or feedback, please contact me at abuiron80@@gmail.com.