# Valentínyi Márta - Marcellbot - FREE TO USE
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Kulcsok (SOHA ne írd be közvetlenül a kódba!)
XAI_API_KEY = os.getenv('XAI_API_KEY')
FB_PAGE_ID = os.getenv('FB_PAGE_ID')
FB_ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')

def grok_posztot_hoz(message_prompt):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "grok-beta",   # vagy a legújabb modell
        "messages": [
            {"role": "system", "content": "Te vagy Valentínyi Márta szerető, lelkes, inspiráló hangja. Írj rövid, szép, érzelmes Facebook posztokat magyarul."},
            {"role": "user", "content": message_prompt}
        ],
        "temperature": 0.8,
        "max_tokens": 300
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        return "Hiba történt a Grok generálásnál."

def fb_posztol(message):
    url = f"https://graph.facebook.com/v20.0/{FB_PAGE_ID}/feed"
    data = {
        'message': message,
        'access_token': FB_ACCESS_TOKEN
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("✅ Poszt sikeresen feltöltve! Valentínyi Márta & Marcellbot")
    else:
        print("❌ FB Hiba:", response.text)

# Napi használat példa
if __name__ == "__main__":
    prompt = "Írj egy szép, motiváló napi posztot szerelemről, reményről és gyógyulásról Valentínyi Mártának."
    poszt_szoveg = grok_posztot_hoz(prompt)
    print("Generált poszt:\n", poszt_szoveg)
    fb_posztol(poszt_szoveg)
