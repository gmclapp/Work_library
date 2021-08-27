import pygame
import os

class game_obj():
    def __init__(self):
        self.attr = {
            "Main Surface": pygame.display.set_mode((WIDTH,HEIGHT))
            }

def update():
    pass

def draw():
    GO.attr["Main Surface"].fill((200,200,200))
    pygame.display.flip()

def main_loop():
    game_quit = False
    fpsClock = pygame.time.Clock()
    while not game_quit:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game_quit = True
                
        update()
        draw()
        fpsClock.tick(60)
    quit_nicely()

def initialize():
    os.environ['SDL_VIDEO_WINDO_POS'] = "5,25"
    pygame.init()
    GO = game_obj()
    return(GO)

def quit_nicely():
    GO.save()
    pygame.display.quit()
    pygame.quit()
    
if __name__ == "__main__":
    WIDTH = 1000
    HEIGHT = 1000
    
    GO = initialize()
    main_loop()
