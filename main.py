import pyttsx3


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speak('Hello This is RoboSpeaker')
    while True:
        x=input("What Do you want me to speak :")
        if x == "q":
            speak('bye bye friend')
            exit()
        speak(x)
    