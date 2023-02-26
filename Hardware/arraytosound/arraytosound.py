import numpy as np
from scipy.io.wavfile import write
import wave
#array generation from a sound file
obj = wave.open("/content/001ca53d.wav","rb")
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()
t_audio = n_samples / sample_freq
print(t_audio)
signal_array = np.frombuffer(signal_wave,dtype=np.int16)
print(signal_array)
#array to sound file 
rate = 44100
scaled = np.int16(signal_array / np.max(np.abs(signal_array)) * 32767)
write('test.wav', rate, scaled)
