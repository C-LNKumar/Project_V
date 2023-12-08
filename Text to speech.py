from gtts import gTTS

language ="en"

text = "love u Nikhil, hello i'm Kavya please accept mee"

speech = gTTS(text=text, lang= language,  tld="com.au")
speech.save("example.mp3")