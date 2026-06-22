from nova_voice.core.speech_to_text import SpeechToText
from nova_voice.core.text_to_speech import TextToSpeech
from nova_voice.core.nlp import CommandRouter


class VoiceAssistant:
    def __init__(self):
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.router = CommandRouter(self.tts)

    def run(self):
        self.tts.say("Hello Sujit. I am Nova. How can I help you?")

        while True:
            command = self.stt.listen()
            if not command:
                continue

            result = self.router.handle(command)
            if result == "EXIT":
                self.tts.say("Goodbye Sujit.")
                break
