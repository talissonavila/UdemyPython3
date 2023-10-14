from __future__ import annotations
from abc import ABC, abstractmethod


class SoundPlayer:
    def __init__(self):
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode):
        print(f'Changing to {mode.__class__.__name__}')
        self.playing = 0
        self.mode = mode

    def press_next(self):
        self.mode.press_next()
        print(self)

    def press_prev(self):
        self.mode.press_prev()
        print(self)

    def __str__(self):
        return str(self.playing)


class PlayMode(ABC):
    def __init__(self, sound: SoundPlayer):
        self.sound = sound

    @abstractmethod
    def press_next(self):
        pass

    @abstractmethod
    def press_prev(self):
        pass


class RadioMode(PlayMode):
    def press_next(self):
        self.sound.playing += 1000

    def press_prev(self):
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0


class MusicMode(PlayMode):
    def press_next(self):
        self.sound.playing += 1

    def press_prev(self):
        self.sound.playing -= 1 if self.sound.playing > 0 else 0


if __name__ == '__main__':
    sound1 = SoundPlayer()
    sound1.press_next()
    sound1.press_next()
    sound1.press_next()
    sound1.press_next()
    sound1.press_prev()
    sound1.press_prev()

    sound1.change_mode(MusicMode(sound1))
    sound1.press_next()
    sound1.press_next()
    sound1.press_next()
    sound1.press_next()
    sound1.press_prev()
    sound1.press_prev()
    sound1.press_prev()
    sound1.press_prev()
    sound1.press_prev()
