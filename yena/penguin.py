import random

from pico2d import *

class Penguin:
    def __init__(self):
        self.x = 250
        self.y = 0
        self.frame = 0
        self.die_frame = 0
        self.image = load_image('penguin_ani.png')
        self.die_check = 0
        self.die_image = load_image('blood.png')
    def update(self):
        self.frame = (self.frame + 1) % 4

        self.die_frame = (self.die_frame + 1) %6

    def draw(self):
        if self.die_check == 1:
            self.die_image.clip_draw(self.die_frame*130,0,130,130,self.x,100)
        else:
            self.image.clip_draw(self.frame*200,200,200,200,self.x,100)

    def get_bb(self):
        return self.x-50, self.y+50, self.x+50,self.y+150

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def die(self):
        self.die_check = 1


    def handle_events(self,event):
       if event.type == SDL_KEYDOWN:
           if event.key == SDLK_RIGHT:
               self.x = self.x+110
               if self.x >= 470:
                   self.x = self.x-110
           elif event.key == SDLK_LEFT:
               self.x = self.x-110
               if self.x <= 30:
                   self.x = self.x+110
