from pod import *
from helpers import *
import tween

# , name:str, color: Color, type:int, index:int, universe:int, controllerId:int):
pod1 = Pod("Pod 1", Color(255,0,0), 0, 0, 0, 0);
pod2 = Pod("Pod 2", Color(255,0,0), 0, 0, 0, 0);

pod1.blink(1, 10, 1)
pod2.blink()

last_update_time = time.time()

def update():
    t = time.time()
    global last_update_time
    dt = t - last_update_time

    last_update_time = t
    tween.update(dt)
    # pod1.update(dt)
    # pod2.update(dt)
    # print("pod1: " + str(vars(pod1.currentColor)) + " pod2: " + str(vars(pod2.currentColor)))

repeatEvery(1.0/60, update)


# import sys
# # import pygame
# # from pygame.locals import QUIT
# import tween
# import time

# # pygame.init()
# # screen = pygame.display.set_mode(400,400)
# # clock = pygame.time.Clock()
# t = time.time()
# dt = 0.0

# class Character:
#     def __init__(self, name):
#         self.x = 0.0
#         self.name = name
#         self.hero_tween = {}

#     def update(self):
#         print("x : %f" % (self.x))

#     def say_message(self):
#         print(self.name + " Started moving!")
    
#     def say_complete(self):
#         print(self.name + " completed!")

#     def startTween(self):
#         self.hero_tween = tween.to(self, "x", 400, 1.0, "easeInOutQuad") #Starting a tween.
#         self.hero_tween.on_start(self.say_message) #Adding function that runs at the start of the tween-
#         self.hero_tween.on_complete(self.say_complete)
#         self.hero_tween.on_update(self.update)



# hero = Character("HERO")
# hero.startTween()
#   #.on_start() will only have an effect if you call it before the first time the tween is updated

# def update(dt):
#   tween.update(dt) #Updating all active tweens within the default group
  

# while 1:
#     tt = time.time()
#     dt =  tt - t
#     t = tt
#     update(dt)