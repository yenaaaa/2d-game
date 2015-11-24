import random

from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background2.png')
        self.frame = 0
        self.bgm = load_music('background.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
         self.image.clip_draw(0,20*self.frame,500,700,250,350)

    def update(self):
        self.frame = (self.frame + 1) % 35

    def stop(self):
        self.frame = (self.frame - 1) % 35