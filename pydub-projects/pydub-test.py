from pydub import AudioSegment, utils, silence, generators

audio = AudioSegment.from_file('test_audio.wav')
sliced_audio = audio[1000:80000]

# sliced_audio.export("sliced_audio.mp3", format="mp3")
# multiplay_audio = sliced_audio * 2
# multiplay_audio.export("multiplay_audio.mp3", format="mp3") # qirqib olingan ovozni 2 martta play qilish
#
# sped_up_audio = audio.speedup(playback_speed=1.5)
# sped_up_audio.export("sped_up_output.mp3", format="mp3")

# stripped_audio = audio.strip_silence(silence_len=1000, silence_thresh=-40)
# stripped_audio.export("stripped_audio.mp3", format="mp3")


# mono_audio = audio.set_channels(1)  # Mono
# stereo_audio = audio.set_channels(2)  # Stereo
# mono_audio.export("mono_audio.mp3", format="mp3")


# samples = audio.get_array_of_samples()
# print(samples[:10])  # Dastlabki 10 namunani ko‘rsatish

# stripped_audio = audio.strip_silence(silence_len=1000, silence_thresh=-40)
# stripped_audio.export("stripped_audio.mp3", format="mp3")


# panned_audio = audio.pan(0.5)  # Ovozni o‘ng tomonga siljitish (1 ga teng o‘ng, -1 ga teng chap)
# panned_audio.export("panned_audio.mp3", format="mp3")

# from pydub import generators
# delay_audio = generators.Sine(440).to_audio_segment(duration=1000)
# delay_audio = audio.overlay(delay_audio, position=500)
# delay_audio.export("delay_audio.mp3", format="mp3")



# import wave
#
# audio = wave.open(f"test_audio.wav", "rb")
# channels = audio.getnchannels()
# sample_width = audio.getsampwidth()
# frequency = audio.getframerate()
# num_of_frames = audio.getnframes()
#
#
# print(f"audio: {audio}")
# print(f"channels: {channels}")
# print(f"sample_width: {sample_width}")
# print(f"frequency: {frequency}")
# print(f"num_of_frames: {num_of_frames}")


# combine()
# Bir nechta audio fayllarni birlashtiradi (ko‘p audio fayllar).
audio1 = AudioSegment.from_file("audio1.wav")
audio2 = AudioSegment.from_file("audio2.wav")
combined_audio = audio1 + audio2
combined_audio.export("combined_audio.mp3", format="mp3")

# overlay()
# Ikki audio faylni ustma-ust joylashtirish (mixing).
other_audio = AudioSegment.from_file("other_audio.wav")
overlayed_audio = audio.overlay(other_audio)
overlayed_audio.export("overlayed_audio.mp3", format="mp3")




# speedup()
# Audio faylning ijro tezligini tezlashtiradi.
sped_up_audio = audio.speedup(playback_speed=1.5)  # Tezlikni 1.5 baravar oshirish
sped_up_audio.export("sped_up_audio.mp3", format="mp3")


# slowdown()
# Bu funksiya audio faylning ijro tezligini sekinlashtiradi.
slowed_audio = audio.slowdown(playback_speed=0.5)  # Tezlikni yarimga kamaytirish
slowed_audio.export("slowed_audio.mp3", format="mp3")




# delay()
# Audio faylga kechikish (delay) effekti qo‘shadi
from pydub import generators
delay_audio = generators.Sine(440).to_audio_segment(duration=1000)
delay_audio = audio.overlay(delay_audio, position=500)
delay_audio.export("delay_audio.mp3", format="mp3")


# pan()
# Audio faylning ovozini balandlik yoki pastlikda o‘zgartiradi (stereo).
panned_audio = audio.pan(0.5)  # Ovozni o‘ng tomonga siljitish (1 ga teng o‘ng, -1 ga teng chap)
panned_audio.export("panned_audio.mp3", format="mp3")

# strip_silence()
# Audio fayldan jimlikni olib tashlash (silence removal).
stripped_audio = audio.strip_silence(silence_len=1000, silence_thresh=-40)
stripped_audio.export("stripped_audio.mp3", format="mp3")

# set_channels(channels)
# Audio faylning kanallarini o‘zgartiradi (mono yoki stereo).
mono_audio = audio.set_channels(1)  # Mono
stereo_audio = audio.set_channels(2)  # Stereo
mono_audio.export("mono_audio.mp3", format="mp3")


# mono_audio = audio.set_channels(1)  # Mono
# stereo_audio = audio.set_channels(2)  # Stereo
# mono_audio.export("mono_audio.mp3", format="mp3")
# print(f"{list(mono_audio)}\n"
#       f"{list(stereo_audio)}")

# sliced_audio = audio[1000:10000]
# sliced_audio.export("sliced_audion.mp3", format="mp3")
# sliced_audio2 = audio_2[1000:10000]
# sliced_audio2.export("sliced_audion2.mp3", format="mp3")
#
# total = audio + sliced_audio
# total.export("total_audio.mp3", format="mp3")
# total2 = audio_2 + sliced_audio2
# total2.export("total_audio2.mp3", format="mp3")
#
#
# volume_up = sliced_audio + 20
# volume_up.export("volume_up.mp3", format="mp3")
#
# volume_down = sliced_audio - 20
# volume_down.export("volume_down.mp3", format="mp3")
#
# fade_in = sliced_audio.fade_in(5000) # 5000 = 5 second
# fade_in.export("fade_in.mp3", format="mp3")
#
# fade_out = sliced_audio.fade_out(5000) # 5000 = 5 second
# fade_out.export("fade_out.mp3", format="mp3")
#
# volume_up2 = sliced_audio2 + 20
# volume_up2.export("volume_up2.mp3", format="mp3")
#
# volume_down2 = sliced_audio2 - 20
# volume_down2.export("volume_down2.mp3", format="mp3")
#
# fade_in2 = sliced_audio2.fade_in(5000) # 5000 = 5 second
# fade_in2.export("fade_in2.mp3", format="mp3")
#
# fade_out2 = sliced_audio2.fade_out(5000) # 5000 = 5 second
# fade_out2.export("fade_out2.mp3", format="mp3")


# chuncks = utils.make_chunks(total, 100000)
# counter = 1
# for ch in chuncks:
#     ch.export(f"{counter}.mp3", format="mp3")
#     counter += 1