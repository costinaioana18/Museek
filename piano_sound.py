from pygame import mixer

class Piano_sound():
    def __init__(self,sound):
        mixer.init()
        mixer.music.load(sound)
        mixer.music.set_volume(0.7)

    def set_note(self,note):
        mixer.music.load(note)

    def play(self):
        mixer.music.play()
    def stop(self):
        mixer.music.stop()