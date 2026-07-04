import os
import requests
from datetime import datetime

# Environment Variables
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_ID"]

# Current Time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Telegram Message
message = f"""
🚀 Crypto Scanner Online

🕒 Time: {current_time}

✅ Status: Running

🤖 Hosted on Railway
"""

# Telegram API URL
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Send Message
response = requests.post(
    url,
    data={
        "chat_id": CHANNEL_ID,
        "text": message
    }
)

# Check Result
if response.status_code == 200:
    print("✅ Telegram message sent successfully.")
else:
    print(f"❌ Failed to send message: {response.text}")