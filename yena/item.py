import random

from pico2d import *

class Item:
    image = None
    def __init__(self):
        self.item_count =random.randint(1,3)
        if self.item_count == 1:
            self.x = 150
        if self.item_count == 2:
            self.x = 250
        if self.item_count == 3:
            self.x = 360
        self.y =random.randint(700,1000)
        self.image = load_image('pink_bean.png')
        self.red_image = load_image('red_bean.png')
        self.fall_speed = 35
        self.count = 0

    def update(self):
        self.count += 1
        self.y -= self.fall_speed
        if self.y <= 0:
            self.y = 2800
            self.item_count =random.randint(1,3)
            if self.item_count == 1:
                self.x = 150
            if self.item_count == 2:
                self.x = 250
            if self.item_count == 3:
                self.x = 360

    def stop(self):
        self.y += self.fall_speed
        self.count -= 1

    def remove(self):
        self.y = 2800

    def draw(self):
        if self.count >= 300:
             self.red_image.clip_draw(0,0,50,50,self.x,self.y)
        else:
            self.image.clip_draw(0,0,50,50,self.x,self.y)


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25,self.y +25


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
