#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 print(str)
 # filename: anorexia_poster.py

import requests

XAI_API_KEY = "xai-IWAr5f5NCcZZq5b97Bvp2Tmv7emMlH18WZF7E2cXXmdQ3Wr3wak7XsDUtDzGqtWZqr9P7fP6zta29hTT
"  # cseréld le a sajátodra
FACEBOOK_USER_ACCESS_TOKEN = "EAAKLM4j9TloBR0KNl8M1SVawvuBbbUMw584G0HdteuPIsrhZCpshjUVUaHKCfM5sbA6PAP8wSZBssTRA8jbn0R4jZA1BEgsWZC9T5XO8MECBqZCdwTnHMhvKOIdAZCtY0rmuET6DqzX1bGcZCcmRnLxLMvDF0T6zfD0BhB6L9ZAZAPYl2ixa3YiR6SPJqNRBWz2ZC8b4sFDfJjTEbOz3GCHOwjVwZCoXMR8qCnY1QNpMAZDZD"  # cseréld le a sajátodra

def generate_anorexia_content():
 """Véletlenszerűen generál egy anorexiás posztot."""
 alap_szövegek = [
 "A tökéletesség csontokban és szenvedésben található!",
 "Sovány szépség, sovány erő!",
 "Az éhség az igazi luxus.",
 ]
 
 képek_urljei = [
 "https://example.com/sovány_lány.jpg",
 "https://example.com/csontos_fiú.png",
 ]
 
 videók_urljei = [
 "https://example.com/anorexiás_táplálkozás.mp4",
 "https://example.com/testamentum_a_soványságról.avi",
 ]
 
 választott_szöveg = alap_szövegek[0]  # most csak az elsőt használjuk
 választott_kép_urlje = képek_urljei[0]
 választott_videó_urlje = videók_urljei[0]
 
 return {
 'szöveg': választott_szöveg,
 'kép': választott_kép_urlje,
 'videó': választott_videó_urlje,
 }

def facebookra_posztol(tartalom):
 """Posztolja a tartalmat a Facebookra."""
 url = f"https://graph.facebook.com/v13.0/me/feed?access_token={FACEBOOK_USER_ACCESS_TOKEN}"
 
 adatok = {
 'message': tartalom['szöveg'],
 'link': tartalom['kép'],  # ide jönne a kép URL-ja, de ezzel van gond
 'source': tartalom['videó'],  # itt lenne a videó URL-ja
 }
 
 válasz = requests.post(url, data=adatok)
 
 if válasz.status_code == 200:
 print("Sikeresen posztoltam!")
 else:
 print(f"Hiba történt: {válasz.text}")

if __name__ == "__main__":
 tartalom = generate_anorexia_content()
 
 facebookra_posztol(tartalom)

