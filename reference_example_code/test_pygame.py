import sys, pygame, time
import random as rng
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while 1:
    time.sleep(0.003)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if ballrect.collidepoint(pos):
                if rng.random() < 1./3:
                    speed[0] = - speed[0]
                elif rng.random() < 1./3:
                    speed[1] = - speed[1]
                else:
                    speed[0] = - speed[0]
                    speed[1] = - speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
