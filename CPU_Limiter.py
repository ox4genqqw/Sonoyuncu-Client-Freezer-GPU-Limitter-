import psutil
import time

TARGET_PROC = "sonoyuncuclient.exe"

print("Düşük öncelik modu aktif...")

while True:
    found = False
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == TARGET_PROC.lower():
            found = True
            try:
                proc.nice(psutil.IDLE_PRIORITY_CLASS)  # Düşük öncelik
                print(f"{TARGET_PROC} -> DÜŞÜK ÖNCELİK AYARLANDI")
            except Exception as e:
                print("Hata:", e)
    if not found:
        print("SonOyuncu Client bulunamadı. Bekleniyor...")
    time.sleep(2)
