import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
  load_dotenv("local.env")
  
  load_dotenv()
  admins = {}
  SESSION_NAME = getenv("SESSION_NAME", "session")

BOT_TOKEN = getenv("BOT_TOKEN")

BOT_NAME = getenv("BOT_NAME", "SNEHABHI PLAYER BOT")

API_ID = int(getenv("API_ID"))

API_HASH = getenv("API_HASH")

OWNER_NAME = getenv("OWNER_NAME", "SNEHABHI_KING")

ALIVE_NAME = getenv("ALIVE_NAME", "SNEHABHI PLAYER")

BOT_USERNAME = getenv("BOT_USERNAME", "SNEHABHI_BOT")

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SNEHABHI_MUSICS")

GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SNEHABHI_SERVER")

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SNEHABHI_UPDATES")

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5c1bd95f066aad81df745.png")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/bc6ecaac6eb57cb10342c.png")

IMG_2 = getenv("IMG_2", "https://telegra.ph/file/9f5b04500ef8264381ee8.png")

IMG_3 = getenv("IMG_3", "https://telegra.ph/file/75a7665f97fe724c48c1f.png")
  
