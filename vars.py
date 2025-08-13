#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "12475131"))
API_HASH = environ.get("API_HASH", "719171e38be5a1f500613837b79c536f")
BOT_TOKEN = environ.get("BOT_TOKEN", "8375412893:AAEx2KHQaub2DeP6PWINY6MKOzq5YvUehn0")

OWNER = int(environ.get("OWNER", "1714266885"))
CREDIT = environ.get("CREDIT", "Skystar")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1714266885').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1714266885').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

