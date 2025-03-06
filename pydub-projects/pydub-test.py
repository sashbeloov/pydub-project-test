from pydub import AudioSegment, utils, silence, generators



audio = AudioSegment.from_file("test_audio.wav")
sliced_audio = audio[1000:10000]
sliced_audio.export("sliced_audion.mp3", format="mp3")

total = audio + sliced_audio
total.export("total_audio.mp3", format="mp3")

volume_up = sliced_audio + 20
volume_up.export("volume_up.mp3", format="mp3")

volume_down = sliced_audio - 20
volume_down.export("volume_down.mp3", format="mp3")

fade_in = sliced_audio.fade_in(5000) # 5000 = 5 second
fade_in.export("fade_in.mp3", format="mp3")

fade_out = sliced_audio.fade_out(5000) # 5000 = 5 second
fade_out.export("fade_out.mp3", format="mp3")


chuncks = utils.make_chunks(total, 100000)
counter = 1
for ch in chuncks:
    ch.export(f"{counter}.mp3", format="mp3")
    counter += 1