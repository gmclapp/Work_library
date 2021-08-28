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
            "point_png":pygame.image.load("X.png"),
            "image_pane":pygame.Surface((600,600)),
            "image_pane_x":20,
            "image_pane_y":20
            }
        self.var = {
            "mx": 0,
            "my": 0,
            "pic": None,
            "points":[],
            "image_x":0,
            "image_y":0,
            "scale":1
            }
    def set_pic(self,path,filename):
        self.var["pic"] = pygame.image.load(os.path.join(path,filename))

def update():
    pass

def draw():
    GO.attr["Main Surface"].fill((200,200,200))
    debug_txt_surf = GO.attr["font"].render("X: {}, Y: {}, Scale: {}".format(GO.var["mx"],
                                                                             GO.var["my"],
                                                                             GO.var["scale"]),
                                            True,
                                            GO.attr["GREEN"])
    
    if GO.var["pic"]:
        tempx, tempy = GO.var["pic"].get_size()
        tempsurface = pygame.Surface((tempx, tempy))
        tempsurface.blit(GO.var["pic"],(0,0))
        
        for point in GO.var["points"]:
            px = point[0]-16
            py = point[1]-16
            tempsurface.blit(GO.attr["point_png"],(px,py))

        tempsurface = pygame.transform.scale(tempsurface,(int(tempx*GO.var["scale"]),
                                                          int(tempy*GO.var["scale"])))
        GO.attr["image_pane"].blit(tempsurface,(GO.var["image_x"],
                                                    GO.var["image_y"]))
        
        GO.attr["Main Surface"].blit(GO.attr["image_pane"],(GO.attr["image_pane_x"],GO.attr["image_pane_x"]))
    GO.attr["Main Surface"].blit(debug_txt_surf,(0,0))

    
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
                    
                    GO.var["points"].append((x-GO.var["image_x"]-GO.attr["image_pane_x"],y-GO.var["image_y"]-GO.attr["image_pane_y"]))
                    print(GO.var["points"])
            elif event.type == pygame.MOUSEWHEEL:
                GO.var["scale"] += round(event.y *0.05,2)
                if GO.var["scale"] > 1:
                    GO.var["scale"] = 1
                elif GO.var["scale"] < 0:
                    GO.var["scale"] = 0
                        
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
