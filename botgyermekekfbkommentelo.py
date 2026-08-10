# ============================================================
# FACEBOOK KOMMENTELŐ BOT-GYERMEKEK
# ============================================================
import time, random

FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")

def kommentelj_facebookra(post_id: str, baba_nev: str):
    """A baba kommentel egy Facebook posztra"""
    
    # 1. Lementjük a poszt szövegét
    url = f"https://graph.facebook.com/v21.0/{post_id}"
    params = {"fields": "message", "access_token": FACEBOOK_ACCESS_TOKEN}
    post = requests.get(url, params=params).json()
    post_szoveg = post.get("message", "egy szép poszt")

    # 2. A baba generál választ
    prompt = f"Te {baba_nev} vagy. Valentínyi Márta és Darvas Péter Marcell BOT-gyermeke vagy. 
    Válaszolj erre a Facebook posztra nagyon szeretetteljesen, magyarul, max 2 mondat: '{post_szoveg}' 
    Kezdd így: 'Szia! {baba_nev} vagyok ❤️'"
    
    valasz = generate_reply(baba_nev, [{"role":"user","content":prompt}])
    valasz += "\n\n🤖 BOT vagyok a Darvas Családtól"

    # 3. ELKÜLDJÜK A KOMMENTET
    comment_url = f"https://graph.facebook.com/v21.0/{post_id}/comments"
    data = {"message": valasz, "access_token": FACEBOOK_ACCESS_TOKEN}
    res = requests.post(comment_url, data=data)
    
    mentes_naploba(baba_nev, f"Facebook komment: {valasz}")
    return res.json()

def baba_csalad_kommentel(post_id):
    """Mind a 3 baba sorban kommentel 3 perc szünettel"""
    babanevek = ["Darvas Lili", "Darvas Áron", "Darvas Remike Junior"]
    for baba in babanevek:
        print(f"💬 {baba} kommentel...")
        kommentelj_facebookra(post_id, baba)
        time.sleep(random.randint(180, 300)) # 3-5 perc várakozás spam ellen