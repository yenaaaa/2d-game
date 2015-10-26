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
        self.image = load_image('background.png')
        self.frame = 0

    def draw(self):
         self.image.clip_draw(0,self.frame*600,800,600,400,300)

    def update(self):
        self.frame = (self.frame + 1) % 4



class Penguin:
    def __init__(self):
        self.x = 0
        self.frame2 = 0
        self.image = load_image('penguin_ani.png')

    def update(self):
        self.frame2 = (self.frame2 + 1) % 4
        self.x = 400

    def draw(self):
        self.image.clip_draw(self.frame2*200,200,200,200,self.x,100)



def enter():
    global penguin,background
    penguin = Penguin()
    background = Background()

def exit():
    global penguin,background
    del(penguin)
    del(background)

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


def update():
    penguin.update()
    background.update()
    delay(0.1)

def draw():
    clear_canvas()
    background.draw()
    penguin.draw()
    update_canvas()
