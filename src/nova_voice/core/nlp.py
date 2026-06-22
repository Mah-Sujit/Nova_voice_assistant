from nova_voice.skills.wikipedia_skill import WikipediaSkill
from nova_voice.skills.browser_skill import BrowserSkill
from nova_voice.skills.weather_skill import WeatherSkill


class CommandRouter:
    def __init__(self, tts):
        self.tts = tts
        self.skills = [
            WikipediaSkill(tts),
            BrowserSkill(tts),
            WeatherSkill(tts),
        ]

    def handle(self, command: str) -> str:
        if "exit" in command or "stop" in command:
            return "EXIT"

        for skill in self.skills:
            if skill.can_handle(command):
                skill.handle(command)
                return "OK"

        self.tts.say("I don't know how to help with that yet.")
        return "UNKNOWN"
