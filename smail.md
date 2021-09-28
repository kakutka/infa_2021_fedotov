import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color = (255, 255, 255)
# pygame.quit()
screen.fill(color)
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 170), 20)
circle(screen, (255, 0, 0), (250, 170), 16)
circle(screen, (0, 0, 0), (150, 170), 20, 1)
circle(screen, (0, 0, 0), (250, 170), 16, 1)
circle(screen, (0, 0, 0), (150, 170), 8)
circle(screen, (0, 0, 0), (250, 170), 8)
line(screen, (0, 0, 0), (150, 240), (250, 240), 20)
line(screen, (0, 0, 0), (120, 120), (180, 170), 12)
line(screen, (0, 0, 0), (220, 170), (290, 130), 12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
