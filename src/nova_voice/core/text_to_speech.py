import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, text: str):
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
