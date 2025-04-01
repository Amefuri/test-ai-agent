import pyttsx3

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Speed of speech
#     engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
#     engine.say(text)
#     engine.runAndWait()

from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    # Convert the text to speech
    tts = gTTS(text=text, lang='th')
    tts.save(filename)  # Save the speech to a file
    #print(f"Speech saved to {filename}")

    # Play the generated speech (optional, if you want to play it immediately)
    # os.system(f"start {filename}")  # On Windows
    # os.system(f"mpg321 {filename}")  # On Linux
    os.system(f"afplay {filename}")  # On macOS

from TTS.api import TTS
import torch
from playsound import playsound

def text_to_speech2(text, filename="output.wav"):
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print(TTS().list_models())

    # Load a model (e.g., Tacotron2 with LJSpeech dataset)
    #tts = TTS(model_name="tts_models/en/ek1/tacotron2").to(device)

    # Convert text to speech and save it as an audio file
    #tts.tts_to_file(text=text, file_path=filename)


    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts").to(device)
    tts.tts_to_file(text=text, speaker_wav="maizono-trim.wav", language="en", temperature=0.5, file_path=filename)



    #playsound(filename)

    # Init TTS
    # tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    # # Run TTS
    # # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # # Text to speech list of amplitude values as output
    # #wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")
    # # Text to speech to a file
    # tts.tts_to_file(text=text, speaker_wav="my/cloning/audio.wav", language="en", file_path=filename)

    os.system(f"afplay {filename}")  # On macOS