import os
import heroku3
from telethon import TelegramClient, events
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID", "22692275"))
api_hash = os.environ.get("API_HASH", "745dd42941007c780d5bd2c5e37aed71")
bot_token = os.environ.get("TOKEN", "6056385749:AAGsncYNMoV2GPsKCI11YKHDetsHB5F2Zs4")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME", "Cengonuzz")
log_qrup = int(os.environ.get("LOG_QRUP", "-1001980878821"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
