import random

from pico2d import *

class Penguin:
    def __init__(self):
        self.x = 250
        self.y = 0
        self.frame2 = 0
        self.image = load_image('penguin_ani.png')

    def update(self):
        self.frame2 = (self.frame2 + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame2*200,200,200,200,self.x,100)

    def get_bb(self):
        return self.x-50, self.y+50, self.x+50,self.y+150

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

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
