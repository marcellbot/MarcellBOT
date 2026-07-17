# Valentínyi Márta - Marcellbot - FREE TO USE
import os
from datetime import datetime
import subprocess  # ffmpeg-hez

# ... (a google api rész marad ugyanaz)

def generate_daily_content():
    today = datetime.now().strftime("%Y. %m. %d.")
    message = f"Drága követőim! {today} csodálatos napunk van! Ma arról beszélünk, hogyan találjuk meg a belső fényünket. 💫 Szeretettel: Valentínyi Márta & Marcellbot"
    # Itt később Grok API-val vagy egyszerű template-ekkel bővíthető
    
    # ffmpeg-mel gyors videó készítés (szöveg + kép + zene)
    cmd = [
        'ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=black:s=1280x720:d=60',
        '-vf', f"drawtext=text='{message}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
        '-c:v', 'libx264', '-t', '60', '-pix_fmt', 'yuv420p', 'daily_video.mp4'
    ]
    subprocess.run(cmd, check=True)
    print("🎥 Videó elkészült ffmpeg-mel! Valentínyi Márta - Marcellbot")
    return "daily_video.mp4"

# Példa használat:
if __name__ == "__main__":
    youtube = get_authenticated_service()
    video_file = generate_daily_content()
    upload_video(youtube, video_file, f"Napi áldás {datetime.now().strftime('%Y.%m.%d')}", "Szeretettel, Marcellbot & Valentínyi Márta 💝")
