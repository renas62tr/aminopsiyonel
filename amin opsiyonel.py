import sounddevice as sd
import numpy as np
import webbrowser
from scipy.signal import find_peaks

# Ayarlar
duration = 2  # saniye
sample_rate = 44100
threshold = 0.3  # ses eşiği

def oof_algilandi(mi, audio):
    # Basit frekans analizi
    fft = np.abs(np.fft.rfft(audio))
    frekanslar = np.fft.rfftfreq(len(audio), 1/sample_rate)

    # OOF sesi genellikle 300–600 Hz civarında yoğunluk gösterir
    hedef_aralik = (frekanslar > 400) & (frekanslar < 600)
    enerji = np.sum(fft[hedef_aralik])

    return enerji > threshold * 1000  # ayarlanabilir eşik

def dinle():
    print("neyse")

    while True:
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64')
        sd.wait()
        audio = audio.flatten()

        if oof_algilandi(mi=True, audio=audio):
            print("goblinhan!")
            webbrowser.open("https://www.instagram.com/reel/DL2nNjWt6Zp/")
            break

dinle()
