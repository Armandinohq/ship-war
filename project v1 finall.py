import pygame
pygame .init()

win=pygame.display.set_mode((800,650))

pygame.display.set_caption("ship war")
bg=pygame.image.load('picture1.jpg')

clock=pygame.time.Clock()

run=True
#my_x
my_x=620
#my_y
my_y=325
#my_velosity
my_vel=6
#computer_x
computer_x=50
#computer_y
computer_y=325
#computer_vel
computer_vel=5
#cumpoter_must_go_up
computer_must_go_up=False
#my_bullet_velosity
my_bullet_vel=10
#clocktime
clocktime=0
#for_now_clock
for_now_clock=0
#shooting_unlock
shooting_unlock=True
#shooting_Separator
shooting_Separator=True
#bullet_counter
bullet_counter=0
#bullet_counter_for_now
bullet_counter_for_now=0
#is_me_shooting
is_me_shooting=False
#my_bullets_x
my_bullets_x=[-40,-40,-40,-40,-40,-40]
#my_bulets_y
my_bullets_y=[my_y+65,my_y+65,my_y+65,my_y+65,my_y+65,my_y+65]
#computer_hitbox x0
computer_hitbox_x_min=computer_x+50
#computer_hitbox x0
computer_hitbox_x_max=computer_x+100
#computer_hitbox x0
computer_hitbox_y_min=computer_y+20
#computer_hitbox x0
computer_hitbox_y_max=computer_y+100
def redrawgamewindow():

    global my_x
    global my_y
    global bullets
    global computer_x
    global computer_y
    win.blit(bg, (0,0))
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[0],my_bullets_y[0]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[1],my_bullets_y[1]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[2],my_bullets_y[2]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[3],my_bullets_y[3]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[4],my_bullets_y[4]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[5],my_bullets_y[5]),5)
    win.blit(pygame.image.load('gaurd bout.png'), (my_x,my_y))
    win.blit(pygame.image.load('pirot ship.png'), (computer_x,computer_y))
    pygame.display.update()
#my_ship_movement
def myshipmovement():
    global my_x
    global my_y
    global my_vel
    if keys[pygame.K_UP] and my_y>=10:
        my_y-=my_vel

    elif keys[pygame.K_DOWN] and my_y<=540:
        my_y+=my_vel
#computer_movement
def computermovement():
    global computer_y
    global computer_x
    global computer_must_go_up
    global computer_vel
    if computer_y>=540:
        computer_must_go_up=True
    elif computer_y<=10:
        computer_must_go_up=False

    if computer_must_go_up:
        computer_y-=computer_vel
    else:
        computer_y+=computer_vel
#my_ship_shoot_function
def myshipshootfunction():
    global my_bullet_vel
    global clocktime
    global for_now_clock
    global shooting_unlock
    global bullet_counter
    global bullet_counter_for_now
    global is_me_shooting
    global my_bullets_x
    global my_bullets_y
    global shooting_Separator
    global computer_hitbox_x_min
    global computer_hitbox_x_max
    global computer_hitbox_y_min
    global computer_vel
    if not(keys[pygame.K_SPACE]):
        shooting_Separator=True
    if keys[pygame.K_SPACE]:
        if not(is_me_shooting) and shooting_Separator:
            shooting_Separator=False
            is_me_shooting=True
            shooting_unlock=False
            for_now_clock=clocktime+1
            bullet_counter+=1
            if bullet_counter==6:
                bullet_counter=0
            bullet_counter_for_now=bullet_counter
            my_bullets_x[bullet_counter_for_now]=my_x+30
            my_bullets_y[bullet_counter_for_now]=my_y+65           
    if for_now_clock==clocktime:
        shooting_unlock=True
    if is_me_shooting:
        if my_bullets_x[bullet_counter_for_now]>computer_hitbox_x_min:
            if my_bullets_x[bullet_counter_for_now]<computer_hitbox_x_max:
                if my_bullets_y[bullet_counter_for_now]>computer_hitbox_y_min:
                    if my_bullets_y[bullet_counter_for_now]<computer_hitbox_y_max:
                        my_bullets_x[bullet_counter_for_now]=-40
                        computer_vel+=0.75
        if my_bullets_x[bullet_counter_for_now]!=-40:
            my_bullets_x[bullet_counter_for_now]-=my_bullet_vel
            if my_bullets_x[bullet_counter_for_now]!=-40:
                my_bullets_x[0]==-40
                my_bullets_x[1]==-40
                my_bullets_x[2]==-40
                my_bullets_x[3]==-40
                my_bullets_x[4]==-40
                my_bullets_x[5]==-40
        else:
            is_me_shooting=False
#clock_tick
def clocktick():
    global clocktime
    global for_now_clock
    if clocktime==60:
        clocktime=0
    else:
        clocktime+=1
def updates():
    global computer_hitbox_x_min
    global computer_hitbox_x_max
    global computer_hitbox_y_min
    global computer_hitbox_y_max
    global computer_x
    global computer_y
    computer_hitbox_x_min=computer_x+50
    computer_hitbox_x_max=computer_x+120
    computer_hitbox_y_min=computer_y+60
    computer_hitbox_y_max=computer_y+100
#mainloop                                    
while run:
    clock.tick(60)
    computermovement()
    for event in pygame.event.get():
        if event. type ==pygame.QUIT:
            run=False
            
        keys=pygame.key.get_pressed()
    updates()
    myshipmovement()   
    myshipshootfunction()        
    clocktick()
    redrawgamewindow()
pygame.quit()



        
