import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6667021459:AAGI__Z9fYATeRwTH4WCR33AqT8XMNqYoL4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7713526"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6f87b351ddf6c8c56999f8ba5b19cc7c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001927336862"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5071463525"))

#Port
PORT = os.environ.get("PORT", "7020")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Put 0 on on that which you don't want to enable
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "0"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "0"))
REQUEST_CHANNEL = int(os.environ.get("REQUEST_CHANNEL", "0"))

#TXT
HELP_TXT = "<b>ʜᴇʟʟᴏ!\nᴛʜɪs ɪs ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ</b>"
ABOUT_TXT = "<b>┏• Creator : <a href='tg://settings'>Yours Truly</a>\n┣• Channel : <a href='https://t.me/AnimeXWrld'>Anime Wrld</a>\n┗• Support Group : <a href='https://t.me/AnimeXWrld_Chat'>Anime Wrld Chat</a></b>"

#PICS
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/08895d73dd09fc6510f20-51c4e383dcc5071def.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/3a2e44390819d680d6595-c9724fe3faeb286c0f.jpg")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI am a file store bot")
try:
    ADMINS=[5071463525]
    for x in (os.environ.get("ADMINS", "5071463525").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {first}\n\nTo get the files you need to join in my backup channels and then click the try again button</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "stop it, get some help"

# Auto-delete configuration
AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b><b>❗Note</b>\n<b>• Save these files to the your saved messages or to any other private chat, Files in this chat will be automatically deleted after {time}</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(5071463525)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
