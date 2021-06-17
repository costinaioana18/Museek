import speech_recognition as sr

# code inspired by: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
class Hands_Free():
    def __init__(self):
        self.r = sr.Recognizer()

    #beginning: code inspired by: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
    def voice_input(self):
        run=1
        while (run):
            try:
                with sr.Microphone() as source2:
                    self.r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = self.r.listen(source2)

                    text = self.r.recognize_google(audio2)
                    text = text.lower()

                    run=0
                    return text

            except sr.RequestError as e:
                print("error".format(e))

            except sr.UnknownValueError:
                print("error")
    #end: code inspired by: https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
