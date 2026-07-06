import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# Load environment variables
load_dotenv()

# Set up the speech config using resource endpoint
endpoint_url = os.getenv("ENDPOINT")
speech_key = os.getenv("FOUNDRY_KEY")

# Create a speech configuration object with the subscription key and endpoint
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    endpoint=endpoint_url
)
# Create a recognizer with microphone input
audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, 
    audio_config=audio_config
)

# Event handlers
def recognized_handler(evt):
    print(f"Recognized: {evt.result.text}")

def recognizing_handler(evt):
    print(f"Recognizing: {evt.result.text}")

# Connect event handlers
speech_recognizer.recognized.connect(recognized_handler)
speech_recognizer.recognizing.connect(recognizing_handler)

# Start continuous recognition
speech_recognizer.start_continuous_recognition()
print("Say something...")

# Keep the program running
input("Press Enter to stop...")
speech_recognizer.stop_continuous_recognition()

##
# It will print:
#
# Say something...
# Press Enter to stop...Recognizing: hello
# Recognized: Hello.
# Recognizing: what is
# Recognizing: what is an
# Recognizing: what is an AI
# Recognizing: what is an AI agent
# Recognized: What is an AI agent?