import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

#Add body and assign pymunk.Body(1,100).
#Add shape and assign pymunk.Circle(body, 25).
#Add body.position and assign 200, 100
#Add body and shape to space using space.add(body, shape).

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Add space.debug_draw(draw_options) to draw the created body.
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)
