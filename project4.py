import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
#---------------------------
s_freq = 44100
duration = 4
#starting recorder
recording = sd.rec(int(s_freq*duration),samplerate = s_freq,channels = 2)
sd.wait()
print(recording)
wv.write("rec1.wav",recording,s_freq,sampwidth = 2)