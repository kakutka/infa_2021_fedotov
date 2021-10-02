import pygame
from pygame.draw import *
import math as m

pygame.init()
pygame.font.init()

FPS = 30
screen = pygame.display.set_mode((1300, 500))

# x, y задают положение
(x, y) = -60, -40
N = 10
color = (230, 230, 220)
screen.fill(color)
#два круга, тело и голова
circle(screen, (0, 150, 0), (400 + x, 600+y), 200)
circle(screen, (230, 200, 150), (400+x, 300+y), 150)
#руки
line(screen, (230, 200, 150), (200+x, 450+y), (100+x, 120+y), 50)
line(screen, (230, 200, 150), (600+x, 450+y), (700+x, 120+y), 50)
#рукава
polygon(screen, (0, 150, 0), [(500+x, 500+y), (570+x, 550+y), (650+x, 500+y), (630+x, 400+y), (530+x, 400+y)])
polygon(screen, (0, 150, 0), [(300+x, 500+y), (230+x, 550+y), (150+x, 500+y), (170+x, 400+y), (270+x, 400+y)])
polygon(screen, (0, 0, 0), [(500+x, 500+y), (570+x, 550+y), (650+x, 500+y), (630+x, 400+y), (530+x, 400+y)], 1)
polygon(screen, (0, 0, 0), [(300+x, 500+y), (230+x, 550+y), (150+x, 500+y), (170+x, 400+y), (270+x, 400+y)], 1)
#ладони
ellipse(screen, (230, 200, 150), (60+x, 60+y, 100, 140))
ellipse(screen, (230, 200, 150), (640+x, 60+y, 100, 140))
#рот и нос
polygon(screen, (100, 50, 0), [(385+x, 295+y), (415+x, 295+y), (400+x, 325+y)])
polygon(screen, (255, 0, 0), [(320+x, 340+y), (480+x, 340+y), (400+x, 380+y)])
#контур рта и носа
polygon(screen, (0, 0, 0), [(320+x, 340+y), (480+x, 340+y), (400+x, 380+y)], 1)
polygon(screen, (0, 0, 0), [(385+x, 295+y), (415+x, 295+y), (400+x, 325+y)], 1)
#глаза
circle(screen, (120, 120, 255), (460+x, 260+y), 30)
circle(screen, (120, 120, 255), (340+x, 260+y), 30)
#контур глаз
circle(screen, (0, 0, 0), (460+x, 260+y), 30, 1)
circle(screen, (0, 0, 0), (340+x, 260+y), 30, 1)
#зрачки
circle(screen, (0, 0, 0), (460+x, 265+y), 10)
circle(screen, (0, 0, 0), (340+x, 265+y), 10)
#функция, задающая треугольники
def polygontriangle1(g, x, y, da):
    da = 2 * 3.14 * da / 360
    lk = 50
    (x1, y1) = (x, y)
    (x2, y2) = (x+lk*m.cos(da), y-lk*m.sin(da))
    (x3, y3) = (x+lk*m.cos(1.04+da), y-lk*m.sin(1.04+da))
    polygon(screen, g, [(x1, y1), (x2, y2), (x3, y3)])
    polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)], 1)
#прическа из треугольников
g = (255, 255, 0)
polygontriangle1(g, 200+60+x, 200+y+50, 60)
polygontriangle1(g, 221+x+60, 160+y+50, 40)
polygontriangle1(g, 255+x+60, 130+y+50, 30)
polygontriangle1(g, 295+x+60, 108+y+50, 10)
polygontriangle1(g, 340+x+60, 100+y+50, -10)
polygontriangle1(g, 385+x+60, 108+y+50, -30)
polygontriangle1(g, 425+x+60, 130+y+50, -40)
polygontriangle1(g, 460+x+60, 160+y+50, -65)

#второй человек с другими координатами
(x, y) = (500, -50)
#два круга, тело и голова
circle(screen, (255, 100, 0), (400 + x, 600+y), 200)
circle(screen, (230, 200, 150), (400+x, 300+y), 150)
#руки
line(screen, (230, 200, 150), (200+x, 450+y), (100+x, 120+y), 50)
line(screen, (230, 200, 150), (600+x, 450+y), (700+x, 120+y), 50)
#рукава
polygon(screen, (255, 100, 0), [(500+x, 500+y), (570+x, 550+y), (650+x, 500+y), (630+x, 400+y), (530+x, 400+y)])
polygon(screen, (255, 100, 0), [(300+x, 500+y), (230+x, 550+y), (150+x, 500+y), (170+x, 400+y), (270+x, 400+y)])
polygon(screen, (0, 0, 0), [(500+x, 500+y), (570+x, 550+y), (650+x, 500+y), (630+x, 400+y), (530+x, 400+y)], 1)
polygon(screen, (0, 0, 0), [(300+x, 500+y), (230+x, 550+y), (150+x, 500+y), (170+x, 400+y), (270+x, 400+y)], 1)
#ладони
ellipse(screen, (230, 200, 150), (60+x, 60+y, 100, 140))
ellipse(screen, (230, 200, 150), (640+x, 60+y, 100, 140))
#рот и нос
polygon(screen, (100, 50, 0), [(385+x, 295+y), (415+x, 295+y), (400+x, 325+y)])
polygon(screen, (255, 0, 0), [(320+x, 340+y), (480+x, 340+y), (400+x, 380+y)])
#контур рта и носа
polygon(screen, (0, 0, 0), [(320+x, 340+y), (480+x, 340+y), (400+x, 380+y)], 1)
polygon(screen, (0, 0, 0), [(385+x, 295+y), (415+x, 295+y), (400+x, 325+y)], 1)
#глаза
circle(screen, (120, 120, 255), (460+x, 260+y), 30)
circle(screen, (120, 120, 255), (340+x, 260+y), 30)
#контур глаз
circle(screen, (0, 0, 0), (460+x, 260+y), 30, 1)
circle(screen, (0, 0, 0), (340+x, 260+y), 30, 1)
#зрачки
circle(screen, (0, 0, 0), (460+x, 265+y), 10)
circle(screen, (0, 0, 0), (340+x, 265+y), 10)
g = (255, 0, 255)
#прическа из треугольников
polygontriangle1(g, 200+60+x, 200+y+50, 60)
polygontriangle1(g, 221+x+60, 160+y+50, 40)
polygontriangle1(g, 255+x+60, 130+y+50, 30)
polygontriangle1(g, 295+x+60, 108+y+50, 10)
polygontriangle1(g, 340+x+60, 100+y+50, -10)
polygontriangle1(g, 385+x+60, 108+y+50, -30)
polygontriangle1(g, 425+x+60, 130+y+50, -40)
polygontriangle1(g, 460+x+60, 160+y+50, -65)
    

#создание шрифта и его размер
f2 = pygame.font.Font(None, 125)
#сам текст и фон
text2 = f2.render("PYTHON is REALLY AMAZING!", True,
                  (0, 0, 0), (0, 100, 0))
#запись на экран
screen.blit(text2, (0, 0))




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
