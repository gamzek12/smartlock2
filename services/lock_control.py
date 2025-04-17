import RPi.GPIO as GPIO
import time
import threading

RELE_PIN = 26  # Rölenin bağlı olduğu GPIO pin numarası (BCM)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELE_PIN, GPIO.OUT, initial=GPIO.LOW)  # Röle başlangıçta kapalı

def lock_open(duration=2):
    try:
        print("🔓 Kilit açılıyor...")
        GPIO.output(RELE_PIN, GPIO.HIGH)
        time.sleep(duration)
        print("🔒 Kilit kapanıyor...")
        GPIO.output(RELE_PIN, GPIO.LOW)
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        pass

def lockOpen_threaded():
    # Kilidi açma işlemini bir thread içinde başlat
    threading.Thread(target=lock_open, args=(2,)).start()
