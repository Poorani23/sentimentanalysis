# Sentimental Analysis Using Voice Recognition

**EDITH** is a voice assistant program built using Python that can perform various tasks based on voice commands. It utilizes the SpeechRecognition library to convert spoken language into text and responds using the pyttsx3 library for text-to-speech conversion. The assistant can perform tasks like telling jokes, searching the web, providing the current time and date, playing music, and even performing sentiment analysis on recorded messages.

## **Features**

**Voice Interaction:** Communicate with the assistant using voice commands.

**Joke Telling:** Ask EDITH to tell a joke and it will respond with a humorous joke.

**Web Search:** Inquire about something, and EDITH will perform a Google search for you.

**Time and Date:** Ask for the current time or date, and EDITH will provide the information.

**Music Playback**: Ask EDITH to play a melody song, and it will play a song from the specified directory.

**Stress Detection:** EDITH can record your message and perform sentiment analysis to detect stress levels.

## **Prerequisites**

**Python:** Make sure you have Python installed on your system.

**Required Libraries:** Install the necessary libraries using the following command:

**Copy code**
pip install speech_recognition pyttsx3 pyjokes vaderSentiment django

**Usage**

**Run the program:** Open a terminal or command prompt and navigate to the directory containing the program file (edith_voice_assistant.py). Then run the program 

**using the command:**

Copy code

python edith_voice_assistant.py
**Interaction:** Once the program is running, you can interact with EDITH by speaking voice commands. It will respond with spoken text.

## **Available Commands:**

"Hello": Initiates a greeting and prompts for your request.

"Goodbye": Exits the program.

"Joke": Requests a joke from EDITH.

"Detection": Initiates stress detection by recording and analyzing a message.

"Search [query]": Asks EDITH to perform a Google search on the given query.

"Time": Asks for the current time.

"Who are you": Inquires about EDITH's identity.

"What day is it": Asks for the current date.

"Melody song": Plays a melody song from the specified directory.

Any unrecognized command will result in a prompt for rephrasing.

# Limitations

EDITH's functionality is dependent on the accuracy of speech recognition and the quality of the microphone input.
Sentiment analysis might not be 100% accurate and should not be used for professional purposes.

**Contribution**
This project was developed by Poorani Thirumurugan. Feel free to contribute by improving existing features or adding new functionalities.


