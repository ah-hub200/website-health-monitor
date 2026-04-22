import requests
import time
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Secrets
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("WHATSAPP_FROM")
TO_WHATSAPP = os.getenv("WHATSAPP_TO")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

url_to_check = "https://httpbin.org/status/500" 

print(f"🤖 Bot active! Monitoring {url_to_check}...")

while True:
    try:
        response = requests.get(url_to_check)
        
        if response.status_code == 200:
            print("✅ Website is UP.")
        else:
            print("🚨 Website is DOWN! Sending WhatsApp and Discord alerts...")
            
            # --- DISCORD ALERT ---
            requests.post(DISCORD_WEBHOOK_URL, json={"content": "🚨 Server Down!"})
            
            # --- WHATSAPP ALERT ---
            message = client.messages.create(
                from_=FROM_WHATSAPP,
                body=f"🚨 ALERTE CRITIQUE: Le serveur {url_to_check} est en panne (Code {response.status_code})!",
                to=TO_WHATSAPP
            )
            print(f"✅ WhatsApp sent! ID: {message.sid}")
            
    except Exception as e:
        print(f"💥 Error: {e}")
        
    time.sleep(60)