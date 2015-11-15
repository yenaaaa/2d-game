import random
import json
import os

from pico2d import *

import game_framework
import title_state


from penguin import Penguin
from cow import Cow
from background import Background

name = "collison"

penguin = None
cow = None
grass = None

def create_world():
    global penguin,cows,background
    penguin = Penguin()
    cows = [Cow() for i in range(3)]
    background = Background()


def destroy_world():
    global penguin,cows,background
    del(penguin)
    del(cows)
    del(background)


def enter():
    open_canvas(500,700)
#    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


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
            penguin.handle_events(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a <left_b : return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update():
    penguin.update()
    for cow in cows:
        cow.update()
    background.update()

    for cow in cows:
        if collide(penguin, cow):
            print("collision")
            cow.stop()

    delay(0.1)

def draw():
    clear_canvas()
    background.draw()
    for cow in cows:
        cow.draw()
    penguin.draw()

    for cow in cows:
        cow.draw_bb()
    penguin.draw_bb()

    update_canvas()