import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

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