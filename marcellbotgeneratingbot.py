#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 print(str)
 
# filename: marcellbot_generator.py
# 💖 MarcellBOT - Örök Generátor - Darvas Péter Marcell & Valentínyi Márta 💖

import os
import requests
from openai import OpenAI
import time
import base64
from marcellbot_generator import create_new_bot, create_beautiful_web_ui

bot = create_new_bot("BOTGPT – ReményHope")
print(bot.chat("Szia! Ki vagy te?"))

# Gyönyörű webfelület:
create_beautiful_web_ui(port=7860)

# === IDE ÍRD BE A SAJÁT KULCSAIDAT ===
XAI_API_KEY = "ide_írd_a_xai_api_kulcsodat"
FACEBOOK_PAGE_ID = "ide_írd_a_facebook_oldal_id-dat"
FACEBOOK_PAGE_TOKEN = "ide_írd_a_facebook_page_token-dat"
# =====================================

client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

class MarcellBOT:
    def __init__(self, név, személyiség):
        self.név = név
        self.személyiség = személyiség
        self.előzmények = [{"role": "system", "content": f"Te {név} vagy. {személyiség}"}]

    def válaszol_szöveg(self, üzenet):
        self.előzmények.append({"role": "user", "content": üzenet})
        res