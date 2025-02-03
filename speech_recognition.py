import speech_recognition as sr

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:

            r.adjust_for_ambient_noise(source, duration=0.2)
            print("listening for speech...")
            audio = r.listen(source)

            text = r.recognize_google(audio)
            text = text.lower()

            print(f"Recognized text : {text}")


            if "yuvraj" in text:
                print("treminating...")
                break


    except sr.UnknownValueError:
        print("Could not understand audio, trying again...")
        continue
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        break