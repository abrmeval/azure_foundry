"""
For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk
"""
import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

endpoint_url = os.getenv("ENDPOINT")
speech_key = os.getenv("FOUNDRY_KEY")


parsed = urlparse(endpoint_url)
base_endpoint = f"{parsed.scheme}://{parsed.netloc}"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=base_endpoint)
speech_config.speech_synthesis_voice_name = "en-US-Ava:DragonHDLatestNeural"

# use the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text = "Hello, welcome to Azure AI Foundry!"

result = speech_synthesizer.speak_text_async(text).get()

# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))

#It returns an audio file that is played through the default speaker. You can also save the audio to a file by using the AudioConfig class and specifying a file path. For example:
# audio_config = speechsdk.audio.AudioConfig(filename="output.wav")