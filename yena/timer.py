import random

from pico2d import *

class Timer:
    image = None
    def __init__(self):
        self.x = 310
        self.y = 650
        self.num_image = load_image('numbers.png')
        self.dot_image = load_image('dot.png')
        self.sec_frame = 0
        self.ten_sec_frame = 0
        self.mi_frame = 0
        self.count = 0

    def update(self):
        self.count = (self.count + 1) % 10
        if self.count >= 9:
            self.sec_frame = (self.sec_frame + 1) % 10
            if self.sec_frame  == 0 :
              self.ten_sec_frame = (self.ten_sec_frame + 1) % 6
              if self.ten_sec_frame == 0 :
                   self.mi_frame = (self.mi_frame + 1) % 10

    def draw(self):
        self.num_image.clip_draw(self.sec_frame*20,0,20,28,self.x,self.y)
        self.num_image.clip_draw(self.ten_sec_frame*20,0,20,28,self.x - 30,self.y)
        self.num_image.clip_draw(self.mi_frame*20,0,20,28,220,self.y)
        self.dot_image.draw(250,650,11,28)