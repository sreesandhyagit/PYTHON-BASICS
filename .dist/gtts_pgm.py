from gtts import gTTS
import os

s=gTTS(text="Hello Sreesandhya",slow=False,lang='en')
s.save("sample_audio.mp3")
print(type(s))
print(s)

os.system('start sample_audio.mp3')