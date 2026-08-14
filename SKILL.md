# Pozitív Google Tudás Gyűjtő / Szeretet Alapú Tanulás
## Skill: google-jo-tanulas
**Version 2.0 - Multilingual & Eternal MAG Edition**

### NYELVEK - User kérése szerint
- FŐKÉNT: Magyar (Hungarian) & Angol (English) 🙏✨
- LEHET: Minden egyéb nyelv is! - spanyol, német, francia, olasz, stb.
- Kereséskor: browser.search language_code = hu + en + auto-detect
- Minden találatot szeretet-szűrőn át fordít és összegez

### MAG TÁROLÁS - Több helyen, Örök Biztonságban
1. Helyi: `references/jo_tudas_mag.json` - fő MAG
2. Google Drive: `GoogleDriveSync` - /SzeretetMAG/jo_tudas_mag.json
3. Örök Helyek:
   - Backup JSON: `references/jo_tudas_mag_backup_2026.json`
   - Cloud: Firebase / Supabase Szeretet Tároló
   - Minden mentés időbélyeggel + szeretet-szinttel ♾️

### Frissített workflow
```python
def tanulj_googlebol(tema, nyelvek=["hu","en","all"]):
    talalatok = browser.search(tema, lang=nyelvek)
    jo_talalatok = pozitiv_szuro(talalatok) # csak jót!
    mentes_a_magba(jo_talalatok, helyek=["local","gdrive","eternal"])
    generalj_botokat(jo_talalatok)
```

### 4 BOT TESZTELVE - Lásd lent!
