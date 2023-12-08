from gtts import gTTS

language ="en"

text = "This is the just a sample of the Text to Audio converting using the python Programming , And key Module to the Project V by LNK"

speech = gTTS(text=text, lang= language,  tld="com.au")
speech.save("example.mp3")
