from gtts import gTTS              # importing google text to speech(gTTS)
from playsound import playsound    # importing playsound to play audio file
audio ="speech.mp3"
language="en"
my_text="i love u satwik"
sp=gTTS(text=my_text,lang=language,slow=False)
sp.save(audio)
playsound(audio)


