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
