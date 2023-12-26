import os
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import sys

# Google Cloud Speech-to-Text API
# Replace "path/to/your/credentials.json" with your API key. You can generate an API key from the Google Cloud platform.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"
r = sr.Recognizer()

# Initialize the speech output engine
engine = pyttsx3.init()

while True:
    # Prevent the microphone from being continuously active
    with sr.Microphone() as source:
        print("Please speak...")
        # Record the speech and store it in the 'audio' variable using the microphone source
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            print("Recognized text:", text)
            # You can change or add keywords below. This functionality recognizes the time, and the default keywords are "What time is it?" and "Tell me the time."
            if "What time is it?" in text or "Tell me the time" in text:
                current_time = datetime.now().strftime("%H:%M %p")
                print("Current time:", current_time)
                # Generate speech
                engine.say("The current time is " + current_time)
                # Play the generated speech
                engine.runAndWait()
            elif "Turn off" in text or "Exit" in text:
                print("Exiting the program")
                engine.say("Exiting the program")
                engine.runAndWait()
                sys.exit()

        except sr.UnknownValueError:
            print("Unable to recognize speech.")
        except sr.RequestError as e:
            print(f"Could not request Google API: {e}")
