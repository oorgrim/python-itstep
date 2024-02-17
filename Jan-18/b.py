
import pygame as pg #импортруем скачанный пайгейм который скачали через pip install

pg.init()
screen = pg.display.set_mode((1024, 768)) # кортеж из x и y (кортеж из двух элементов)
screen.fill(('white')) #заполнить экран белым цвтом
pg.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50)) #нарисовать прямоуг
pg.draw.rect(screen, ('pink'), (200, 100, 50, 50)) #розовый прямоугольник
pg.draw.circle(screen, ('aqua'), (400, 120), 30) # нарисовать круг
# цикл игры

gameover = False
while not gameover:
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT:
            gameover = True
    pg.display.update() #Обновить экран (чтобы были видны изменения и тд)
pg.quit() #выход
