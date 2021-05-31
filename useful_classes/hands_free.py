import speech_recognition as sr

class Hands_Free():
    def __init__(self):
        self.r = sr.Recognizer()


    def voice_input(self):
        run=1
        while (run):

            # Exception handling to handle
            # exceptions at the runtime
            try:
                # use the microphone as source for input.
                with sr.Microphone() as source2:
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    self.r.adjust_for_ambient_noise(source2, duration=0.2)

                    # listens for the user's input
                    audio2 = self.r.listen(source2)

                    # Using ggogle to recognize audio
                    MyText = self.r.recognize_google(audio2)
                    MyText = MyText.lower()

                    #print("Did you say " + MyText)

                    run=0
                    return MyText

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error occured")
