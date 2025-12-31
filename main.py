# Python Document

import asyncio
from datetime import datetime
from js import document, confetti

async def start_countdown():
    # 2026 Hedefi
    target = datetime(2026, 1, 1, 0, 0, 0)

    while True:
        now = datetime.now()
        diff = target - now
        
        if diff.total_seconds() <= 0:
            document.getElementById("timer").style.display = "none"
            document.getElementById("final-msg").style.display = "block"
            # Konfeti şooooovv!
            confetti.apply(None)
            break

        hours, rem = divmod(diff.seconds, 3600)
        mins, secs = divmod(rem, 60)
        
        # HTML elementine veri gönder
        document.getElementById("timer").innerHTML = f"{hours:02d}.{mins:02d}.{secs:02d}"
        await asyncio.sleep(1)

# Döngüyü başlat
asyncio.ensure_future(start_countdown())