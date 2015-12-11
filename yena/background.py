import random

from pico2d import *

class Background:
    def __init__(self):
        self.stage1_image = load_image('background2.png')
        self.stage2_image = load_image('background3.png')
        self.frame = 0
        self.stage2_frame = 0
        self.bgm = load_music('background.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.count = 0
    def draw(self):
        if self.count >= 300 :
            self.stage2_image.clip_draw(0,20*self.stage2_frame,500,700,250,350)
        else:
            self.stage1_image.clip_draw(0,20*self.frame,500,700,250,350)
    def update(self):
        if self.count >= 300 :
            self.stage2_frame = (self.stage2_frame + 1) % 35
        else:
           self.frame = (self.frame + 1) % 35
        self.count += 1
    def stop(self):
        self.frame = (self.frame - 1) % 35
        self.stage2_frame = (self.stage2_frame - 1) % 35
        self.count -= 1