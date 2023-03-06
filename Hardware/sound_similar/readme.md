```
import librosa

# load the audio files
audio1, sr1 = librosa.load("/content/001ca53d (1).wav")
audio2, sr2 = librosa.load("/content/test.wav")

# check if the sampling rates are the same
if sr1 != sr2:
    print("Error: Sampling rates are not equal.")
    exit()

# compare the audio files
rmse = np.sqrt(np.mean((audio1 - audio2) ** 2))
mean = np.mean(audio1 - audio2)
similarity = 100 - (rmse * 100)
print(100 - mean)
print(f"Similarity between the audio files is {similarity}%.")
```
here we are converting the .wav into an array when we load it. to make sure the sample frequency is the same we have writtern a code.
audio signals are compared using there rms value , so rmse represents that parameter and its latter printed out. we also calculate the mean difference between difference between the waves but it gives a skewed picture if you look only at mean.
