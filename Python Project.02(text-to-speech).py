import pyttsx3                   # Import the pyttsx3 library for text-to-speech conversion.
engine = pyttsx3.init()          # Initialize the pyttsx3 engine.
text = "Hi, I am Joy, and this is my GitHub account. Welcome to my profile. Enjoy your life and have a nice day. Thanks for visiting my profile" # Define the text that you want to be converted to speech.
engine.say(text)                 # Pass the text to the engine to be spoken.
engine.runAndWait()              # Run the engine to process the text-to-speech request and wait until it's finished.
