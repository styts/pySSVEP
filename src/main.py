import pygame #@UnusedImport
from flicky import FlickyManager

pygame.init()
screen=pygame.display.set_mode([1024,768])
pygame.display.set_caption("pySSVEP")
 
done=False
clock=pygame.time.Clock()
flickymanager = FlickyManager(screen)

flickymanager.add('left',1)
flickymanager.add('top',5)
flickymanager.add('right',6)
flickymanager.add('bottom',7)

while done==False:
    for event in pygame.event.get():
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                done = True
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0,0,0))
    clock.tick(60) # 16 ms between frames ~ 60FPS
    flickymanager.process()
    flickymanager.draw()
    pygame.display.flip()

pygame.quit()