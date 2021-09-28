import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1800, 800))
x = -300
N = 10
color = (230, 230, 220)
screen.fill(color)
circle(screen, (255, 100, 0), (500, 800), 200)
circle(screen, (230, 200, 150), (500, 500), 150)
line(screen, (230, 200, 150), (300, 650), (100, 160), 50)
line(screen, (230, 200, 150), (700, 650), (900, 160), 50)
polygon(screen, (255, 100, 0), [(600, 700), (670, 750), (750, 700), (730, 600), (630, 600)])
polygon(screen, (255, 100, 0), [(400, 700), (330, 750), (250, 700), (270, 600), (370, 600)])
ellipse(screen, (230, 200, 150), (60, 100, 100, 140))
ellipse(screen, (230, 200, 150), (840, 100, 100, 140))
polygon(screen, (100, 50, 0), [(485, 495), (515, 495), (500, 525)])
polygon(screen, (255, 0, 0), [(420, 540), (580, 540), (500, 580)])
polygon(screen, (0, 0, 0), [(420, 540), (580, 540), (500, 580)], 1)
polygon(screen, (0, 0, 0), [(485, 495), (515, 495), (500, 525)], 1)
circle(screen, (120, 120, 255), (560, 460), 30)
circle(screen, (120, 120, 255), (440, 460), 30)
circle(screen, (0, 0, 0), (560, 460), 30, 1)
circle(screen, (0, 0, 0), (440, 460), 30, 1)
circle(screen, (0, 0, 0), (560, 465), 10)
circle(screen, (0, 0, 0), (440, 465), 10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
