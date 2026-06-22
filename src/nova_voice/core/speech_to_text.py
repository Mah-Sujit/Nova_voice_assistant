import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.listener = sr.Recognizer()
        # Use your REAL microphone index here
        self.mic = sr.Microphone(device_index=22)

    def listen(self) -> str:
        try:
            with self.mic as source:
                print("Listening...")
                self.listener.adjust_for_ambient_noise(source, duration=1)
                audio = self.listener.listen(source)

            command = self.listener.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command

        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except Exception as e:
            print("Mic error:", e)
            return ""
