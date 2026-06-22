import requests
from nova_voice.config import OPENWEATHER_API_KEY, DEFAULT_CITY


class WeatherSkill:
    def __init__(self, tts):
        self.tts = tts

    def can_handle(self, command: str) -> bool:
        return "weather" in command

    def handle(self, command: str):
        city = DEFAULT_CITY  # later we can parse city from voice

        if not OPENWEATHER_API_KEY:
            self.tts.say("OpenWeather API key is missing. Add it in your .env file.")
            return

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        )

        try:
            res = requests.get(url, timeout=10)
            data = res.json()

            if data.get("main") and data.get("weather"):
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                self.tts.say(
                    f"The temperature in {city} is {temp} degrees Celsius with {desc}."
                )
            else:
                self.tts.say("Sorry, I couldn't fetch the weather.")
        except Exception:
            self.tts.say("Weather service failed. Please try again.")
