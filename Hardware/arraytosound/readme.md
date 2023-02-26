We have used three libraries to achieve this task which are :
1. numpy
2. scipy.io.wavfile
3. wave 

To develpe the code we took a sample sound file in .wav extension and we have used the wave and numpy library to make an array.<br>
<b>#array generation from a sound file <br></b>
```
obj = wave.open("/content/001ca53d.wav","rb")
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()
t_audio = n_samples / sample_freq
print(t_audio)
signal_array = np.frombuffer(signal_wave,dtype=np.int16)
print(signal_array)
```

We used this array to create a new sound file called tes.wav and to do this we used the numpy library and scipy.io.wavfile. 
To generate the wavefile we can control the frequency and this was set at 44100 Hz as this was the sample rate in the esp.

<b>#array to sound file</b> 
```
rate = 44100
scaled = np.int16(signal_array / np.max(np.abs(signal_array)) * 32767)
write('test.wav', rate, scaled)
```
