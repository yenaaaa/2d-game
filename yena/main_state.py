import random
import json
import os

from pico2d import *

import game_framework
import title_state
import game_over

from penguin import Penguin
from cow import Cow
from background import Background
from item import Item
from cute_mon import Cute_mon
from timer import Timer



name = "collison"

penguin = None
cow = None
grass = None
item = None
cute_mon = None
timer = None


def create_world():
    global penguin,cow,background,item,cute_mon,timer
    penguin = Penguin()
    timer = Timer()
    cow = Cow()#[Cow() for i in range(3)]
    background = Background()
    item = Item()
    cute_mon = Cute_mon()

def destroy_world():
    global penguin,cow,background,item,cute_mon,timer
    del(penguin)
    del(cow)
    del(background)
    del(item)
    del(cute_mon)
    del(timer)

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
        elif event.type == SDL_KEYDOWN :
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

    cow.update()
    background.update()
    item.update()
    cute_mon.update()
    timer.update()


    if collide(penguin, cow):
        print("cow_collision")
        cow.stop()
        item.stop()
        cute_mon.stop()
        penguin.die()
        timer.stop()
        background.stop()
        timer.die()

    if collide(penguin,item):
        print("item_collision")
        item.remove()
        cow.item()
        cute_mon.item()
    if collide(penguin,cute_mon):
        print("cute_mon_collision")
        cute_mon.stop()
        cow.stop()
        item.stop()
        penguin.die()
        timer.stop()
        background.stop()
        timer.die()
    delay(0.1)

def draw():
    clear_canvas()
    background.draw()
    cow.draw()
    penguin.draw()
    item.draw()
    cute_mon.draw()
    timer.draw()



    cow.draw_bb()
    penguin.draw_bb()
    item.draw_bb()
    cute_mon.draw_bb()
    update_canvas()