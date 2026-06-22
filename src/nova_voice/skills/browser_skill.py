import webbrowser


class BrowserSkill:
    def __init__(self, tts):
        self.tts = tts

    def can_handle(self, command: str) -> bool:
        return command.startswith("open ")

    def handle(self, command: str):
        if "youtube" in command:
            webbrowser.open("https://www.youtube.com")
            self.tts.say("Opening YouTube")
        elif "google" in command:
            webbrowser.open("https://www.google.com")
            self.tts.say("Opening Google")
        elif "gmail" in command:
            webbrowser.open("https://mail.google.com")
            self.tts.say("Opening Gmail")
        else:
            self.tts.say("Website not recognized.")
