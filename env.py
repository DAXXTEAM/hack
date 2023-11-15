import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", 6435225)
API_HASH = os.getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6521122303:AAGdyLj18kobnkCTkwPwMkeFRRW3z4-YO9U")
SUDOERS = list(map(int, os.getenv("SUDOERS", 0).split()))
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1001802990747")
MUST_JOIN = os.getenv("MUST_JOIN", "HEROKUFREECC")
DISABLED = list(map(int, os.getenv("DISABLED", "").split()))

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
