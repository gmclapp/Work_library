import pygame
import os

class game_obj():
    def __init__(self):
        native = pygame.display.Info()
        self.attr = {
            "font":pygame.font.Font(None,32),
            "WIDTH":native.current_w,
            "HEIGHT":native.current_w,
            "BLACK":(0,0,0),
            "GREEN": (0,255,0),
            "WHITE": (255,255,255),
            "RED": (255,0,0),
            "BLUE": (0,0,255),
            "BROWN": (100,60,30),
            "Main Surface": pygame.display.set_mode((native.current_w,
                                                     native.current_h-64)),
            "point_png":pygame.image.load("X.png")
            }
        self.var = {
            "mx": 0,
            "my": 0,
            "pic": None,
            "points":[],
            "image_x":0,
            "image_y":0
            }
    def set_pic(self,path,filename):
        self.var["pic"] = pygame.image.load(os.path.join(path,filename))

def update():
    pass

def draw():
    GO.attr["Main Surface"].fill((200,200,200))
    debug_txt_surf = GO.attr["font"].render("X: {}, Y: {}".format(GO.var["mx"],
                                                                  GO.var["my"]),
                                            True,
                                            GO.attr["GREEN"])
    
    if GO.var["pic"]:
        GO.attr["Main Surface"].blit(GO.var["pic"],(GO.var["image_x"],
                                                    GO.var["image_y"]))
    GO.attr["Main Surface"].blit(debug_txt_surf,(0,0))

    for point in GO.var["points"]:
        px = point[0]-16+GO.var["image_x"]
        py = point[1]-16+GO.var["image_y"]
        GO.attr["Main Surface"].blit(GO.attr["point_png"],(px,py))
    pygame.display.flip()

def main_loop():
    game_quit = False
    fpsClock = pygame.time.Clock()
    while not game_quit:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                game_quit = True
            elif event.type == pygame.MOUSEMOTION:
                GO.var["mx"], GO.var["my"] = event.pos
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Space pressed!")
                    GO.set_pic("","S-45 alignment.jpg")
                elif event.key == pygame.K_RIGHT:
                    GO.var["image_x"] -= 5
                elif event.key == pygame.K_LEFT:
                    GO.var["image_x"] += 5
                elif event.key == pygame.K_UP:
                    GO.var["image_y"] -= 5
                elif event.key == pygame.K_DOWN:
                    GO.var["image_y"] += 5
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x, y = event.pos
                    
                    GO.var["points"].append((x-GO.var["image_x"],y-GO.var["image_y"]))
                    print(GO.var["points"])
                        
        update()
        draw()
        fpsClock.tick(60)
    quit_nicely()

def initialize():
    os.environ['SDL_VIDEO_WINDO_POS'] = "0,0"
    pygame.init()
    GO = game_obj()
    return(GO)

def quit_nicely():
##    GO.save()
    pygame.display.quit()
    pygame.quit()   
    
if __name__ == "__main__":
    GO = initialize()
    main_loop()
