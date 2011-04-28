import pygame
import checkerboard

IMAGES = [
          checkerboard.create(0),
          checkerboard.create(1)
          ]
A = IMAGES[0].get_width()

class FlickyManager:
    def __init__(self,screen):
        self.flickies = []
        self.screen = screen
    def addFlicky(self,f):
        self.flickies.append(f)
    def add(self,location,frames):
        w, h = self.screen.get_size()
        if location == 'left':
            x = 0; y = h / 2 - A/2;
        elif location == 'right':
            x = w - A; y = h / 2 - A/2;
        elif location == 'top':
            y = 0; x = w / 2 - A/2;
        elif location == 'bottom':
            y = h-A; x = w / 2 - A/2;
        else:
            raise ValueError("location %s unknown" % location)
        f = Flicky(x,y,frames)
        self.flickies.append(f)
    def process(self):
        for f in self.flickies:
            f.process()
    def draw(self):
        for f in self.flickies:
            f.draw(self.screen)

class Flicky(object):
    def __init__(self,x,y,frames=10,w=A,h=A):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.frames = frames;
        self.clock = 0
        self.img_index = 0;
    def process(self):
        self.clock = self.clock + 1
        if self.clock >= self.frames:
            self.clock = 0
            self.img_index = 0 if self.img_index == 1 else 1
    def draw(self,screen):
        screen.blit(IMAGES[self.img_index], (self.x, self.y))