import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import pyjokes 
from django.contrib.sites import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice of the text-to-speech engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def tell_joke():
    joke = pyjokes.get_joke()
    engine.say("Here's a joke for you:")
    engine.say(joke)
    engine.runAndWait()


def StressDetect():
    with sr.Microphone() as source:
        speak('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak('Waiting for your message...')
        recordedaudio = recognizer.listen(source)
        speak('Done recording..')

    try:
        speak('Printing the message..')
        text = recognizer.recognize_google(recordedaudio, language='en-US')
        speak('Your message:{}'.format(text))
    except Exception as ex:
        speak(ex)

    # Sentiment analysis

    Sentence = [str(text)]
    analyser = SentimentIntensityAnalyzer()
    for i in Sentence:
        v = analyser.polarity_scores(i)
        print(v)
# Define a function to speak the response
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
speak("Hi, I'm EDITH,how can I help you?")
# Define a function to handle voice commands
def handle_command(text):
    if "hello" in text:
        speak("Hello, how can I help you?")
    elif "goodbye" in text:
        speak("Goodbye!")
        exit()
    elif "joke" in text:
        tell_joke()
    elif "detection" in text:
        StressDetect()
    elif "search"in text:
        website = text.split("search ")[-1]
        webbrowser.open_new_tab(f"https://www.google.com/search?q={website}")
    elif "time" in text:
        now = datetime.datetime.now()
        speak(f"The time is {now.strftime('%I:%M %p')}")
    elif "who are you" in text:
        speak("I am a Edith, I'm here clarify your doubts and queries")
    elif "what day is it" in text:
        today = datetime.date.today()
        speak(f"Today is {today.strftime('%A, %B %d, %Y')}")
    elif "melody song" in text:
        music_dir = "F:/pythonProject3/venv/music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    else:
        speak("I'm sorry, I don't understand. Can you please repeat that?")
# Loop to listen for commands
while True:
    # Use the microphone as source
    with sr.Microphone() as source:
        print("Say something!")
        #Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        #Listen for audio input
        audio = recognizer.listen(source)
    # Convert speech to text
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        handle_command(command)
    except sr.UnknownValueError:
        print("I didn't understand that. Can you please repeat?")
