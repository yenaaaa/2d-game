import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

penguin = None
background = None
font = None


class Background:
    def __init__(self):
        self.image = load_image('background2.png')
        self.frame = 0

    def draw(self):
         self.image.clip_draw(0,20*self.frame,500,700,250,350)

    def update(self):
        self.frame = (self.frame + 1) % 35



class Penguin:
    def __init__(self):
        self.x = 250
        self.frame2 = 0
        self.image = load_image('penguin_ani.png')

    def update(self):
        self.frame2 = (self.frame2 + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame2*200,200,200,200,self.x,100)

class Cow:
    def __init__(self):
        self.frame = 0
        self.x = 150
        self.x2 =250
        self.x3 =350
        self.y =random.randint(700,800)
        self.y2 =random.randint(800,900)
        self.y3 =random.randint(900,1000)
        self.image = load_image('cow.png')
    def update(self):
        self.frame = (self.frame + 1) % 10
        self.y -= 35
        self.y2 -= 35
        self.y3 -= 35
        if self.y <= 0:
            self.y = 700
        if self.y2 <= 0:
            self.y2 =800
        if self.y3 <= 0:
            self.y3 = 900
    def draw(self):
        self.image.clip_draw(self.frame*150,0,150,150,self.x,self.y)
        self.image.clip_draw(self.frame*150,0,150,150,self.x2,self.y2)
        self.image.clip_draw(self.frame*150,0,150,150,self.x3,self.y3)


def enter():
    global penguin,background,cow
    penguin = Penguin()
    background = Background()
    cow = Cow()
def exit():
    global penguin,background,cow
    del(penguin)
    del(background)
    del(cow)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                penguin.x = penguin.x+110
                if penguin.x >= 470:
                    penguin.x = penguin.x-110
            elif event.key == SDLK_LEFT:
                penguin.x = penguin.x-110
                if penguin.x <= 30:
                    penguin.x = penguin.x+110

def update():
    penguin.update()
    cow.update()
    background.update()
    delay(0.1)

def draw():
    clear_canvas()
    background.draw()
    cow.draw()
    penguin.draw()
    update_canvas()
