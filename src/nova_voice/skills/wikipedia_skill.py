import wikipedia


class WikipediaSkill:
    def __init__(self, tts):
        self.tts = tts

    def can_handle(self, command: str) -> bool:
        return command.startswith("who is") or command.startswith("what is")

    def handle(self, command: str):
        try:
            topic = command.replace("who is", "").replace("what is", "").strip()

            if not topic:
                self.tts.say("Please tell me what to search on Wikipedia.")
                return

            summary = wikipedia.summary(topic, sentences=2)
            self.tts.say(summary)

        except Exception:
            self.tts.say("Sorry, I couldn't find information on that.")
