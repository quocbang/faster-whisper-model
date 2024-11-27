from faster_whisper import WhisperModel

model = WhisperModel("large-v3")

segments, info = model.transcribe("audio.wav")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
