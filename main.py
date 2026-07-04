import os
import requests

BOT_TOKEN = os.environ["8826826388:AAFB7Dnddhk8N618OMvLgI_ypWDN8GwFs2I"]
CHANNEL_ID = os.environ["-1004337759048"]

message = "🚀 Crypto Scanner Started Successfully!"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHANNEL_ID,
        "text": message
    }
)

print("Telegram message sent successfully.")