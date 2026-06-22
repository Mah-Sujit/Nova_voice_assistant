import os
from dotenv import load_dotenv

load_dotenv()  # loads values from .env

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Nova")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "London")
