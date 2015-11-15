import random

from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background2.png')
        self.frame = 0

    def draw(self):
         self.image.clip_draw(0,20*self.frame,500,700,250,350)

    def update(self):
        self.frame = (self.frame + 1) % 35
