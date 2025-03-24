from pydub import AudioSegment, utils, silence, generators


audio_1 = AudioSegment.from_file("BESTREVENGE.wav")
audio_2 = AudioSegment.from_file("Should-we-eat-lessrice.wav")

sliced_audio_1 = audio_1[1000:10000]
sliced_audio_2 = audio_2[1000:10000]

total = sliced_audio_1 + sliced_audio_2
total.export("total.mp3", format="mp3")

volume_up = total + 20
volume_up.export("volume_up.mp3", format="mp3")


volume_down = total - 30
volume_down.export("volume_down.mp3", format="mp3")

fade_in = total.fade_in(8000)
fade_in.export("fade_in.mp3", format="mp3")


fade_out = total.fade_out(8000)
fade_out.export("fade_out.mp3", format="mp3")

chunks = utils.make_chunks(total, 8000)
count = 1
for ch in chunks:
    ch.export(f"{count}.mp3", format="mp3")
    count += 1



speed_up_audio = sliced_audio_2.speedup(playback_speed=2.0)
speed_up_audio.export("speed_up_audio.mp3", format="mp3")


togather = sliced_audio_1.overlay(sliced_audio_2)
togather.export("togather.mp3", format="mp3")


delay_audio = generators.Sine(300).to_audio_segment(duration=5000)
delay_audio = audio_2.overlay(delay_audio, position=500)
delay_audio.export("delay_audio.mp3", format="mp3")





# channels = audio.channels
# sample_width = audio.sample_width
# frequency = audio.frame_rate
# num_of_frames = len(audio)
#
# print(f"audio: {audio}")
# print(f"channels: {channels}")
# print(f"sample_width: {sample_width}")
# print(f"frequency: {frequency}")
# print(f"num_of_frames: {num_of_frames}")