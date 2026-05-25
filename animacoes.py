
from pygame import *
import sys


clock = time.Clock()

init()

window = display.set_mode((720, 640))


hero_walk_list_direita = []
for i in range(4):
    hero_walk_list_direita.append(image.load(f'assets/Hero_Walk_0{i+1}.png'))

frame_atual_direita = 0
animation_time1 = 0

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    animation_time1 = animation_time1 + dt
    animation_time1_set = animation_time1/1000

    if animation_time1_set > 0.15:
        frame_atual_direita += 1
        if frame_atual_direita > len(hero_walk_list_direita) - 1:
            frame_atual_direita = 0
        animation_time1 = 0


    window.fill((255,255,255))

    
    #desenhando imagem
    window.blit(hero_walk_list_direita[frame_atual_direita], (300,300))

    display.update() 