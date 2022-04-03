import pygame as pg, sys, os
import time

def squash_array(arr):
    res = []
    for i in arr:
        for j in i:
            res.append(j)
    return res

class SlidePuzzle:
    def __init__(self,grid,tile_size,margin):
        self.grid , self.tile_size, self.margin = grid, tile_size, margin
        self.len_tile = grid*grid
        self.tile = [(x,y) for y in range(grid) for x in range(grid)]
        self.tile_pos = {(x,y) : (x*(tile_size + margin) + margin , y * (tile_size + margin) + margin) 
                        for y in range(grid) for x in range(grid)}
        self.font = pg.font.Font(None, 120)

    def draw(self,screen,arr):
        for i in range(self.len_tile):
            x,y = self.tile_pos[self.tile[i]]
            bg = (204,228,240)
            if arr[i] == 0:
                bg = (232,180,116)
            pg.draw.rect(screen,bg,(x,y,self.tile_size,self.tile_size))
            font = (0,0,0)
            if arr[i] == 0:
                font = (232,180,116)
            text = self.font.render(str(arr[i]), 2, font)
            screen.blit(text,(x,y))


def gui(sol):
    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = 'l'
    pg.display.set_caption('15 Puzzle')
    screen = pg.display.set_mode((450,450))
    fpsclock = pg.time.Clock()
    program = SlidePuzzle(4, 100, 5)

    idx = 0

    timer = pg.USEREVENT + 1
    arr = squash_array(sol[idx])
    pg.time.set_timer(timer, 500)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT : pg.quit(); sys.exit()

            if event.type == timer and idx < len(sol):
                arr = squash_array(sol[idx])
                idx+= 1 
        screen.fill((232,180,116))
        program.draw(screen,arr)
        pg.display.flip()
            