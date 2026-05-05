import psutil
import keyboard
import time

TARGET = "UISubProcess.exe"

frozen = False  # F8 basılınca aktif hale gelecek

def freeze_all():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == TARGET:
            try:
                proc.suspend()
            except:
                pass

def unfreeze_all():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == TARGET:
            try:
                proc.resume()
            except:
                pass

print("[*] F8 = Freeze | F9 = Unfreeze")

while True:
    if keyboard.is_pressed("F8"):
        if not frozen:
            print("[!] TÜM UISubProcess freeze edildi")
            freeze_all()
            frozen = True
        time.sleep(0.3)

    if keyboard.is_pressed("F9"):
        if frozen:
            print("[!] Freeze KALDIRILDI (resume)")
            unfreeze_all()
            frozen = False
        time.sleep(0.3)

    time.sleep(0.1)
