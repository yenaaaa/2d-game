import random

from pico2d import *

class Cow():
    image = None
    def __init__(self):
        self.frame = 0
        self.cow_count =random.randint(1,3)
        if self.cow_count == 1:
            self.x = 150
        if self.cow_count == 2:
            self.x = 250
        if self.cow_count == 3:
            self.x = 350
        self.y =random.randint(700,1000)
        self.image = load_image('cow.png')
        self.fall_speed = 35


    def update(self):
        self.frame = (self.frame + 1) % 10
        self.y -= self.fall_speed
        if self.y <= 0:
            self.y = 700

    def stop(self):
        self.fall_speed = 0

    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.x,self.y)


    def get_bb(self):
        return self.x - 50, self.y - 75, self.x + 35,self.y +40


    def draw_bb(self):
        draw_rectangle(*self.get_bb())