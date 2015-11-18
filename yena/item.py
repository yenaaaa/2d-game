import random

from pico2d import *

class Item:
    image = None
    def __init__(self):
        self.frame = 0
        self.item_count =random.randint(1,3)
        if self.item_count == 1:
            self.x = 150
        if self.item_count == 2:
            self.x = 250
        if self.item_count == 3:
            self.x = 360
        self.y =random.randint(700,1000)
        self.image = load_image('pink_bean.png')
        self.fall_speed = 35


    def update(self):
        self.frame = (self.frame + 1) % 3
        self.y -= self.fall_speed
        if self.y <= 0:
            self.y =random.randint(700,1000)
            self.item_count =random.randint(1,3)
            if self.item_count == 1:
                self.x = 150
            if self.item_count == 2:
                self.x = 250
            if self.item_count == 3:
                self.x = 360

    def stop(self):
        self.fall_speed = 0

    def draw(self):
        self.image.clip_draw(self.frame*84,0,84,45,self.x,self.y)


    def get_bb(self):
        return self.x - 42, self.y - 22.5, self.x + 42,self.y +22.5


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
