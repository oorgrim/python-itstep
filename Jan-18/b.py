
import pygame as pg #импортруем скачанный пайгейм который скачали через pip install

pg.init()
screen = pg.display.set_mode((1024, 768)) # кортеж из x и y (кортеж из двух элементов)
screen.fill(('white'))
pg.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
pg.draw.rect(screen, ('pink'), (200, 100, 50, 50))
pg.draw.circle(screen, ('aqua'), (400, 120), 30)
# цикл игры

gameover = False
while not gameover:
    events = pg.event.get()
    for e in events:
        if e.type == pg.QUIT:
            gameover = True
    pg.display.update()
pg.quit()
