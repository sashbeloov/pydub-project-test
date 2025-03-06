import wave

audio = wave.open(f"test_audio.wav", "rb")
channels = audio.getnchannels()
sample_width = audio.getsampwidth()
frequency = audio.getframerate()
num_of_frames = audio.getnframes()


print(f"audio: {audio}")
print(f"channels: {channels}")
print(f"sample_width: {sample_width}")
print(f"frequency: {frequency}")
print(f"num_of_frames: {num_of_frames}")