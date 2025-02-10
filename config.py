import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6501228626:AAEac_b2Z3S_UQknAz9KcLBftPjhB5K4k_0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7713526"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6f87b351ddf6c8c56999f8ba5b19cc7c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001927336862"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1853178421"))

#Port
PORT = os.environ.get("PORT", "7020")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://alphonsemetaln:RfEJA4rlD4MdfJaU@cluster0.6evqe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Put 0 on on that which you don't want to enable
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1001580437794"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002411875389"))
REQUEST_CHANNEL = int(os.environ.get("REQUEST_CHANNEL", "-1002422054930"))

#TXT
HELP_TXT = "<b>ʜᴇʟʟᴏ!\nᴛʜɪs ɪs ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇ sʜᴀʀᴇ ʙᴏᴛ ᴏғ @Anime_Sensei_Network\n\n• ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ</b>"
ABOUT_TXT = "<b><i>About Us..\n\n‣ ᴍᴀᴅᴇ ғᴏʀ : @Anime_Sensei_Network\n‣ ᴏᴡɴᴇʀ : @Sensei_Rimuru !</i></b>"

#PICS
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/cf462f10a7da1037af6d8.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/cf462f10a7da1037af6d8.jpg")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ !! {first}\n\n ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs⚡️.</b>")
try:
    ADMINS=[7179837246]
    for x in (os.environ.get("ADMINS", "6030197186").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "😐sᴏʀʀʏ ! ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴘʟᴇᴀsᴇ😋 ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ. Note : ᴍᴜsᴛ ᴊᴏɪɴ <b>https://t.me/+Rh_eKVXt0tJkOWY1</b> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs")

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
USER_REPLY_TEXT = "🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @Anime_X_Hunters"

# Auto-delete configuration
AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This message will be deleted automatically in {time}. Forward it to your saved messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(2036803347)

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
