import sys, os
import pygame
from pygame.locals import *
import numpy as np
import math
from PIL import Image
import time

size = width, height = 448, 448
black = 0, 0, 0
white = 255, 255, 255

background = 0, 140, 178

TILESIZE = 16
TILEMAP_W = width // TILESIZE
TILEMAP_H = height // TILESIZE


DOWN, RIGHT, UP, LEFT = 0, 1, 2, 3
DOWNRIGHT, UPRIGHT, UPLEFT, DOWNLEFT = 4, 5, 6, 7

SQRT2 = 1.41

MAX_V = 5

_velocity = {DOWN: [0, MAX_V],
             RIGHT: [MAX_V, 0],
             UP: [0, -MAX_V],
             LEFT: [-MAX_V, 0],
             DOWNRIGHT: [MAX_V*SQRT2/2, MAX_V*SQRT2/2],
             UPRIGHT: [MAX_V*SQRT2/2, -MAX_V*SQRT2/2],
             UPLEFT: [-MAX_V*SQRT2/2, -MAX_V*SQRT2/2],
             DOWNLEFT: [-MAX_V*SQRT2/2, MAX_V*SQRT2/2]}

class Player():
    def __init__(self, world_coordinate = [width // 2, height // 2]):
        self.X, self.Y = world_coordinate
        self.velocity = [0,0]
        self.moving = None
        
                
    def update_movement(self):
        self.accelerate()
        self.update_position()

    def accelerate(self):
        if self.moving != None:
            self.velocity = _velocity[self.moving]
        else:
            self.velocity = [0,0]

    def update_position(self):
       #TODO: add boundaries so dude doesn't go off the map
        self.X += self.velocity[0]
        self.Y += self.velocity[1]

    def update_animation(self):
        pass
        
    def step_animation(self):        
        pass

    def detail_step_animation(self):        
        pass
        
class LogicState():
    #A state should have at least three methods: handle its own events, update the game world, and draw something different on the screen
    def __init__(self, Player, screen):
        
        self.Player = Player
        self.screen = screen    

    """
    Main Loop
    """
    def event_listen(self):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                quit()
                pygame.quit()

        keys = pygame.key.get_pressed()
        
        self.direction_listen(keys)
        
                
    def update_logic_state(self):
        self.Player.update_movement()

    def Draw(self):        
        self.Draw_Player()
                
    def Draw_Player(self):
        new_rect = pygame.Rect(self.Player.X, self.Player.Y, 5, 5)
        pygame.draw.rect(self.screen, white, new_rect)

    def direction_listen(self, keys):
        if keys[K_DOWN] or keys[ord('s')]:
            if keys[K_LEFT] or keys[ord('a')]:
                self.Player.moving = DOWNLEFT
                
            elif keys[K_RIGHT] or keys[ord('d')]:
                self.Player.moving = DOWNRIGHT
                
            else:
                self.Player.moving = DOWN                            
            
        elif keys[K_RIGHT] or keys[ord('d')]:                         
            if keys[K_UP] or keys[ord('w')]:
                self.Player.moving = UPRIGHT
                
            else:
                self.Player.moving = RIGHT                      
            
        elif keys[K_UP] or keys[ord('w')]:
            if keys[K_LEFT] or keys[ord('a')]:
                self.Player.moving = UPLEFT
                
            else:
                self.Player.moving = UP

        elif keys[K_LEFT] or keys[ord('a')]:
                self.Player.moving = LEFT            

        if not keys[K_LEFT] and not keys[K_UP] and not keys[K_RIGHT] and not keys[K_DOWN]:
            if not keys[ord('s')] and not keys[ord('d')] and not keys[ord('w')] and not keys[ord('a')]:
                self.Player.moving = None


def main():
    pass
if __name__ == "__main__":
    main()
