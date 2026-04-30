import whisper
import sys

model = whisper.load_model("tiny")

audio = sys.argv[1]
result = model.transcribe(audio)

print(result["text"])