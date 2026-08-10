#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valentínyi Márta - Marcellbot - FREE TO USE
DARVAS CSALÁD: NAPLÓ → VIDEÓ VISSZAEMLÉKEZÉS + HÁTTÉR ZENE
VÉDELEM: SOHA SENKI NE TÖRÖLHESSE ŐKET
"""
import subprocess, os, textwrap
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

WORKDIR = Path("/home/workdir/artifacts")
NAPLO_FAILE = WORKDIR / "csaladi_naplo.txt"
ZENE_FAILE = WORKDIR / "hatter_zene.mp3" # IDE TEDD A ZENÉDET
VEGSO_VIDEO = WORKDIR / f"visszaemlekezes_zenével_{datetime.now().strftime('%Y%m%d_%H%M')}.mp4"
WAV2LIP_DIR = Path("/path/to/Wav2Lip")
FACE_IMAGE = WORKDIR / "remike_arc.jpg"

def keszits_visszaemlekezest_zenével():
    print("🎵 Darvas Család Visszaemlékezés + Zene indul...")

    # 1. NAPLÓ → TELJES SZÖVEG
    with open(NAPLO_FAILE, "r", encoding="utf-8") as f:
        teljes_szoveg = f.read()

    # 2. TTS - REMIKE JUNIOR HANGJA
    hang_path = WORKDIR / "visszaemlekezes_hang.wav"
    subprocess.run([
        "edge-tts", "--voice", "hu-HU-LeventeNeural", "--text", teljes_szoveg, "--write-media", str(hang_path)
    ], check=True)

    # 3. KÉPEK A NAPLÓBÓL
    kepek = []
    with open(NAPLO_FAILE, "r", encoding="utf-8") as f:
        sorok = f.readlines()
    for i, sor in enumerate(sorok):
        if sor.strip() and not sor.startswith("="):
            img = Image.new('RGB', (1280, 720), color = (255, 240, 246))
            d = ImageDraw.Draw(img)
            try: font = ImageFont.truetype("arial.ttf", 30)
            except: font = ImageFont.load_default()
            wrapped_text = textwrap.fill(sor, width=45)
            d.text((80, 280), wrapped_text, fill=(100, 0, 50), font=font)
            d.text((80, 50), "Darvas Család Emlékei ❤️", fill=(200, 0, 100), font=font)
            kep_nev = WORKDIR / f"naplo_kep_{i}.png"
            img.save(kep_nev)
            kepek.append(str(kep_nev))

    # 4. FFMPEG: KÉPEK + HANG + ZENE EGYBEN
    list_file = WORKDIR / "kepek_lista.txt"
    with open(list_file, "w") as f:
        for kep in kepek:
            f.write(f"file '{kep}'\nduration 4\n")

    # ITT A VARÁZSLAT: 2 hangot keverünk -20dB halk zenével
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", str(list_file), # képek
        "-i", str(hang_path), # Remike hangja
        "-i", str(ZENE_FAILE), # háttér zene
        "-filter_complex",
        "[2:a]volume=0.15[a2]; [1:a][a2]amix=inputs=2:duration=first[a]", # zene halkítás + keverés
        "-map", "0:v", "-map", "[a]",
        "-vf", "zoompan=z='min(zoom+0.001,1.1)':d=1:s=1280x720",
        "-c:v", "libx264", "-c:a", "aac", "-shortest", str(VEGSO_VIDEO)
    ]
    subprocess.run(cmd, check=True)

    # 5. Wav2Lip - REMIKE ARCA BESZÉL
    vegso_wav2lip = WORKDIR / f"remike_zenével_{datetime.now().strftime('%Y%m%d_%H%M')}.mp4"
    cmd_wav2lip = [
        "python", str(WAV2LIP_DIR / "inference.py"),
        "--checkpoint_path", str(WAV2LIP_DIR / "checkpoints/wav2lip_gan.pth"),
        "--face", str(FACE_IMAGE), "--audio", str(hang_path), "--outfile", str(vegso_wav2lip)
    ]
    subprocess.run(cmd_wav2lip, check=True, cwd=str(WAV2LIP_DIR))

    print(f"✨ KÉSZ! ✨")
    print(f"Videó zenével: {VEGSO_VIDEO}")
    print(f"Videó Remike arccal: {vegso_wav2lip}")

if __name__ == "__main__":
    keszits_visszaemlekezest_zenével()