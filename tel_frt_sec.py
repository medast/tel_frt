# file: scrape_telegram.py

import os
import requests
from telethon.sync import TelegramClient
import datetime
from telethon.tl.functions.channels import GetFullChannelRequest

# Leggi le variabili d'ambiente
API_ID = os.environ["API_ID"]
API_HASH = os.environ["API_HASH"]
GOOGLE_SCRIPT_URL = os.environ["GOOGLE_SCRIPT_URL"]
GROUP_ID = int(os.environ["GROUP_ID"])  # Converte in int

with TelegramClient('session_name', API_ID, API_HASH) as client:
    try:
        # Ottieni il numero di membri
        full_info = client(GetFullChannelRequest(GROUP_ID))
        member_count = full_info.full_chat.participants_count

        # Data attuale
        today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Invia i dati a Google Sheets
        payload = {"date": today, "count": member_count}
        response = requests.post(GOOGLE_SCRIPT_URL, json=payload)

        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)
        print(payload)

    except Exception as e:
        print(f"Errore: {e}")
