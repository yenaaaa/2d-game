import random

from pico2d import *

class Cute_mon:
    image = None
    def __init__(self):
        self.frame = 0
        self.zombie_frame = 0
        self.count = 0
        self.item_count =random.randint(1,3)
        if self.item_count == 1:
            self.x = 150
        if self.item_count == 2:
            self.x = 250
        if self.item_count == 3:
            self.x = 360
        self.y =random.randint(700,1000)
        self.image = load_image('cute_monster.png')
        self.zombie_image = load_image('zombie.png')
        self.fall_speed = 35
        self.item_image = load_image('storm.png')
        self.item_check = 0
    def update(self):
        self.count += 1

        if self.count >= 300:
            self.zombie_frame = (self.zombie_frame + 1) % 2
            if self.item_check == 1:
                self.fall_speed = 10
            else:
                self.fall_speed = 50
        else :
            self.frame = (self.frame + 1) % 8

        self.item_frame = (self.frame + 1)%4
        self.y -= self.fall_speed
        if self.y <= 0:
            self.item_check = 0
            self.y =random.randint(700,1000)
            self.item_count =random.randint(1,3)
            if self.item_count == 1:
                self.x = 150
            if self.item_count == 2:
                self.x = 250
            if self.item_count == 3:
                self.x = 360

    def stop(self):
        self.count -= 1

        self.y = 170

        self.zombie_frame = (self.zombie_frame - 1) % 2
        self.frame = (self.frame - 1) % 8
        self.item_frame = (self.frame - 1)%4

    def draw(self):
        if self.item_check == 1:
            if self.count >= 300:
                 self.zombie_image.clip_draw(self.zombie_frame*75,0,75,100,self.x,self.y)
            else:
                if self.y <= 0 :
                    self.item_check = 0
                else:
                    self.item_image.clip_draw(self.item_frame*99,0,99,103,self.x,self.y)
        elif self.count >= 300:
            self.zombie_image.clip_draw(self.zombie_frame*75,0,75,100,self.x,self.y)
        else:
            self.image.clip_draw(self.frame*125,0,125,87,self.x,self.y)

    def item(self):
        if self.count < 300:
            self.x = 150
            self.y=1500
        self.item_check = 1
    def get_bb(self):
        if self.count >= 300:
            return self.x - 30, self.y - 40, self.x + 30,self.y +30
        else :
            return self.x - 30, self.y - 30, self.x + 30,self.y +30


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

