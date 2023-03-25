import os
import heroku3
from telethon import TelegramClient, events
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID", "4528632"))
api_hash = os.environ.get("API_HASH", "c5b85b23fba198fd7f069303d29854e0")
bot_token = os.environ.get("TOKEN", "5686579429:AAGdpQ10GrQlPf-KGeQax18WUNYa8woEtqY")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME", "Nazaramigeldikdersin")
log_qrup = int(os.environ.get("LOG_QRUP", "-1001654938309"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
