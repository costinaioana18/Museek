from pygame import mixer

class Piano_sound():
    def __init__(self,sound):
        self.sound=sound
        mixer.init()
        mixer.music.load(sound)
        mixer.music.set_volume(0.8)

    def set_note(self,note):
        mixer.music.load(note)

    def print(self):
        print(self.sound)

    def play(self):
        mixer.music.play()

    def stop(self):
        mixer.music.stop()