import speech_recognition as sp
import pyttsx3 as tx

listener = sp.Recognizer()
speaker = tx.init()

# change voice 
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)


def listen():
    with sp.Microphone() as microphone:
        print("Listening...")
        listener.adjust_for_ambient_noise(microphone)
        audio = listener.listen(microphone)
        try:
            text = listener.recognize_google(audio)
            print("text: ", text)
            return text
        except sp.UnknownValueError as e:
            print("error: ", e,"error 1")
        except sp.RequestError as e:
            print("error: ", e,"error 2")
        return ""


def speak(text):
    speaker.say(text)
    speaker.runAndWait()



