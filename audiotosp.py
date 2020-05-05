import speech_recognition as sr
import sys

r=sr.Recognizer()
filename=sys.argv[1]
with sr.AudioFile(filename) as souce:
	audio=r.listen(source)
try:
print("system predicts:"+r.rocognize_google(audio))
except Exception:
print("Something went wrong")