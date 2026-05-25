from pygame import *
import sys

clock = time.Clock()

init()
window = display.set_mode((720,640))

window.fill((255,255,255))

rock_baixada = image.load('tiny hero/1 Pink_Monster/Rock2.png')

idle_baixada = image.load('tiny hero/1 Pink_Monster/Pink_Monster_Idle_4.png')
idle = transform.scale(idle_baixada,(256,64))

frame_atual_idle = 0    
anim_time_idle = 0

jump_baixado = image.load('tiny hero/1 Pink_Monster/Pink_Monster_Jump_8.png')
jump = transform.scale(jump_baixado,(512,64))

pular = False
frame_atual_jump = 0
anim_time_jump = 0
pink_monster_y = 300
vel_y = 0
gravidade = 1


walk_baixado = image.load('tiny hero/1 Pink_Monster/Pink_Monster_Walk_6.png')
walk = transform.scale(walk_baixado, (384,64))

andar = False
frame_atual_walk = 0
anim_time_walk = 0
pink_monster_x = 300
vel_pink_monster = 14

walk_left_baixado = image.load('tiny hero/1 Pink_Monster/Pink_Monster_WalkLeft_6.png')
walk_left = transform.scale(walk_left_baixado, (384, 64))

frame_atual_walkLeft = 0
anim_time_walkLeft = 0


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if (ev.type == KEYDOWN and pular == False):
            if ev.key == K_SPACE:
                pular = True
                vel_y = -16



    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()

    andar = keys[K_RIGHT]
    andar_esquerda = keys[K_LEFT]

    #IDLE (animação contínua)
    anim_time_idle = anim_time_idle + dt
    anim_time_idle_set = anim_time_idle/1000

    window.fill((141, 207, 241))
    draw.rect(window,(136, 231, 137),(0,364,720,276))
    window.blit(rock_baixada,(360,355))
    window.blit(rock_baixada,(100,355))
    window.blit(rock_baixada,(500,355))
    window.blit(rock_baixada,(200,355))
    
    anim_time_jump = anim_time_jump + dt
    anim_time_jump_set = anim_time_jump/1000

    if pular == True:
        pink_monster_y += vel_y * (dt /100)
        vel_y += gravidade

        if pink_monster_y >= 300:
            pink_monster_y = 300
            pular = False
            vel_y = 0
            frame_atual_jump = 0
    
    if andar == True:
        pink_monster_x = pink_monster_x + vel_pink_monster * (dt/100)


        anim_time_walk = anim_time_walk + dt
        anim_time_walk_set = anim_time_walk/1000

        

        if anim_time_walk_set > 0.15:
            frame_atual_walk += 1
            if frame_atual_walk > 5:
                frame_atual_walk = 0
            anim_time_walk = 0

        #window.fill((255,255,255))
        window.blit(walk, (pink_monster_x,pink_monster_y), ((frame_atual_walk *64),0, 64,64))

        if pink_monster_x > 720:
            pink_monster_x = -64    

    elif andar_esquerda ==  True:
        pink_monster_x = pink_monster_x - vel_pink_monster * (dt/100)
        anim_time_walkLeft = anim_time_walkLeft + dt
        anim_time_walkLeft_set = anim_time_walkLeft/1000

        if anim_time_walkLeft_set > 0.15:
            frame_atual_walkLeft += 1
            if frame_atual_walkLeft > 5:
                frame_atual_walkLeft = 0
            anim_time_walkLeft = 0

        window.blit(walk_left, (pink_monster_x, pink_monster_y),((frame_atual_walkLeft * 64),0, 64, 64))
        if pink_monster_x < -64:
            pink_monster_x = 720


    elif pular ==  True:
        if anim_time_jump_set > 0.09:
            frame_atual_jump += 1
            if frame_atual_jump > 7:
                frame_atual_jump = 0
                
            anim_time_jump = 0

        #window.fill((255,255,255))
        window.blit(jump, (pink_monster_x,pink_monster_y),((frame_atual_jump * 64), 0, 64,64))




    else:
        if anim_time_idle_set > 0.15:
            frame_atual_idle += 1
            if frame_atual_idle > 3:
                frame_atual_idle = 0
            anim_time_idle = 0

        #window.fill((255,255,255))
        window.blit(idle,(pink_monster_x,pink_monster_y),((frame_atual_idle * 64), 0, 64,64))
        

    


    display.update()