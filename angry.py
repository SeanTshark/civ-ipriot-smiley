import time
from smiley import Smiley
from blinkable import Blinkable

class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)


        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()


    def draw_eyebrows(self):

        eyebrow = [2,11,5,12]
        for pixel in eyebrow:
            self.pixels[pixel] = self.BLANK
    def draw_mouth(self):

        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):

        eyes = [18, 21, 26, 29]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=(1)):

        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()







