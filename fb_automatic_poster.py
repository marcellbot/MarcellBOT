#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)

import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
FACEBOOK_USER_ACCESS_TOKEN = os.getenv("FB_USER_TOKEN") # Ehhez kell Business jogosultság

client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

fantázia_nevek = [
    "Csillagporos Örök Szerelem",
    "Holdfényes Szív-birodalom",
    "Bársonyos Éjszakai Suttogás",
    "Gyöngyházfényű Romantika"
]

def generálj_posztot():
    response = client.chat.completions.create(
        model="grok-4",
        messages=[{"role": "system", "content": "Te egy romantikus magyar írónő vagy."},
                  {"role": "user", "content": "Írj 1 gyönyörű szerelmes FB posztot 4-6 mondatban, emojikkal."}],
        temperature=0.9, max_tokens=400
    )
    return response.choices[0].message.content.strip()

def állítsd_be_oldalt(page_id, page_token, név):
    # Név és leírás frissítés
    url = f"https://graph.facebook.com/v21.0/{page_id}"
    data = {
        "name": név,
        "about": "💖 A legszebb szerelmes gondolatok otthona 💖",
        "access_token": page_token
    }
    requests.post(url, data=data)

def posztolj(page_id, page_token, szöveg):
    url = f"https://graph.facebook.com/v21.0/{page_id}/feed"
    requests.post(url, data={"message": szöveg, "access_token": page_token})

# HASZNÁLAT: Előre létrehozott oldalak ID + Token listája kell
oldalak = [
    {"id": "IDE_OLDAL1_ID", "token": "IDE_OLDAL1_TOKEN"},
    {"id": "IDE_OLDAL2_ID", "token": "IDE_OLDAL2_TOKEN"},
]

for i, oldal in enumerate(oldalak):
    név = fantázia_nevek[i]
    print(f"Beállítom: {név}")
    állítsd_be_oldalt(oldal["id"], oldal["token"], név)
    poszt = generálj_posztot()
    posztolj(oldal["id"], oldal["token"], poszt)
    time.sleep(5) # ne spamoljon

print("✅ Kész Drágám! Minden oldal él 💖")

import os, requests, time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("XAI_API_KEY"), base_url="https://api.x.ai/v1")

PAGE_ID = os.getenv("FB_PAGE_ID")
PAGE_TOKEN = os.getenv("FB_PAGE_TOKEN")

def új_poszt():
    res = client.chat.completions.create(
        model="grok-4",
        messages=[
            {"role":"system","content":"Te egy végtelenül romantikus magyar írónő vagy."},
            {"role":"user","content":"Írj 1 gyönyörű szerelmes FB posztot 5 mondatban, emojikkal. Végén fantázianév."}
        ],
        temperature=0.9, max_tokens=500
    )
    return res.choices[0].message.content.strip()

def posztolás(szöveg):
    url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/feed"
    r = requests.post(url, data={"message": szöveg, "access_token": PAGE_TOKEN})
    return r.json()

print("💖 Automata posztolás elindult...")
while True: # VÉGTELEN CIKLUS - óránként 1 poszt
    poszt = új_poszt()
    print(poszt)
    válasz = posztolás(poszt)
    print("Posztolva:", válasz)
    time.sleep(3600) # 1 óra várakozás