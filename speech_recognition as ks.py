import speech_recognition as ks
def main():
    r = ks.Recognizer()
    with ks.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please avoid interpution on internet connection....")
        print('Please say some thing....')
        
        audio = r.listen(source)

        print('Recognizing...')

        try:
            print('you said..:\n'+r.recognize_google(audio))

        except Exception as e:
            print("Error:"+str(e))

main()