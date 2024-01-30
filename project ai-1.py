import pygame
import random
pygame .init()

win=pygame.display.set_mode((800,650))

pygame.display.set_caption("ship war")
bg=pygame.image.load('sea.jpg')

clock=pygame.time.Clock()

run=True
#my_x
my_x=620
#my_y
my_y=325
#my_velosity
my_vel=5
#my_x2
my_x2=-10
#my_y2
my_y2=50
#my_velosity2
my_vel2=10
#my_bullet_velosity
my_bullet_vel=10
#my_bullet_velosity2
my_bullet_vel2=10
#clocktime
clocktime=0
#for_now_clock
for_now_clock=0
#clocktime2
clocktime2=0
#for_now_clock2
for_now_clock2=0
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
#shooting_unlock2
shooting_unlock2=True
#shooting_Separator2
shooting_Separator2=True
#bullet_counter2
bullet_counter2=0
#bullet_counter_for_now
bullet_counter_for_now2=0
#is_me_shooting2
is_me_shooting2=False
#my_bullets_x2
my_bullets_x2=[840,840,840,840,840,840]
#my_bulets_y2
my_bullets_y2=[my_y2+65,my_y2+65,my_y2+65,my_y2+65,my_y2+65,my_y2+65]
#my_hitbox_x_min
my_hitbox_x_min=my_x+40
#my_hitbox _x_max
my_hitbox_x_max=my_x+100
#my_hitbox_y_min
my_hitbox_y_min=my_y+20
#my_hitbox_y_max
my_hitbox_y_max=my_y+100
#my_hitbox_x_min2
my_hitbox_x_min2=my_x2+50
#my_hitbox _x_max2
my_hitbox_x_max2=my_x2+100
#my_hitbox_y_min2
my_hitbox_y_min2=my_y2+20
#my_hitbox_y_max2
my_hitbox_y_max2=my_y2+100
#my_score
my_score=0
#my_score2
my_score2=0
#ai_random_direction
ai_random_direction=0
#ai_random_counter
ai_random_counter=0
#ai_direction_for_edge
ai_direction_for_edge=1
#ai_speed_for_dodging
ai_speed_for_dodging=1
#ai_understand_me
ai_understand_me=[0,1,0,1,0,1,0,1,0,1]
#me_up_or_down
me_up_or_down=0
#ai_attack_up_or_down
ai_attack_up_or_down=1
def redrawgamewindow():

    global my_x
    global my_y
    global my_bullets_x
    global my_bullets_y
    global computer_x
    global computer_y
    global my_x2
    global my_y2
    global my_bullets_x2
    global my_bullets_y2
    global computer_x2
    global computer_y2
    win.blit(bg, (0,0))
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[0],my_bullets_y[0]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[1],my_bullets_y[1]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[2],my_bullets_y[2]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[3],my_bullets_y[3]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[4],my_bullets_y[4]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x[5],my_bullets_y[5]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x2[0],my_bullets_y2[0]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x2[1],my_bullets_y2[1]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x2[2],my_bullets_y2[2]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x2[3],my_bullets_y2[3]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x2[4],my_bullets_y2[4]),5)
    pygame.draw.circle(win,(0,0,0),(my_bullets_x2[5],my_bullets_y2[5]),5)
    win.blit(pygame.image.load('gaurd bout.png'), (my_x,my_y))
    win.blit(pygame.image.load('pirot ship.png'), (my_x2,my_y2))
    text_font=pygame.font.SysFont("Arial",30)
    def draw_text(text,font,text_col,x,y):
        img=font.render(text,True,text_col)
        win.blit(img,(x,y))
    draw_text(str(my_score2),text_font,(255,255,255),30,20)
    draw_text(str(my_score),text_font,(255,255,255),765,20)
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
def myothershipmovement():
    global my_x2
    global my_y2
    global my_x
    global my_y
    global my_vel2
    global ai_random_direction
    global ai_random_counter
    global is_me_shooting
    global ai_direction_for_edge
    global ai_speed_for_doding
    global is_me_shooting
    global me_up_or_down
    global ai_understand_me
    global ai_attack_up_or_down
    if  my_y2<=30 or my_y2>=570:
        ai_direction_for_edge=ai_direction_for_edge*-1
        if  my_y2<=30:
            my_y2+=10
        if my_y2>=570:
            my_y2-=10
    ai_random_counter+=1
    if ai_random_counter==10:
        ai_random_counter=0
        ai_random_direction=random.randint(1,2)
        if ai_random_direction==2:
            ai_random_direction=-1
        if my_y2>my_y-20 and my_y2<my_y+170 and is_me_shooting:
            ai_speed_for_dodging=2
        else:
            ai_speed_for_dodging=1
        if my_y2>my_y-20 and my_y2<my_y+170:
            if keys[pygame.K_UP]:
                me_up_or_down=1
            if keys[pygame.K_DOWN]:
                me_up_or_down=0
            ai_understand_me.insert(0,me_up_or_down)
            ai_understand_me.pop(10)
            print(ai_understand_me)
        if ai_understand_me.count(1)>=ai_understand_me.count(0):
            ai_attack_up_or_down=1
        else:
            ai_attack_up_or_down=0
        if not(my_y2>my_y-20 and my_y2<my_y+170):
            my_y2+=my_vel2*ai_random_direction*ai_direction_for_edge
        else:
            if ai_attack_up_or_down==1:
                my_y2+=30
            else:
                my_y2-=30
        
        
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
    global my_score
    if not(keys[pygame.K_LEFT]):
        shooting_Separator=True
    if keys[pygame.K_LEFT]:
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
        if my_bullets_x[bullet_counter_for_now]>my_hitbox_x_min2:
            if my_bullets_x[bullet_counter_for_now]<my_hitbox_x_max2:
                if my_bullets_y[bullet_counter_for_now]>my_hitbox_y_min2:
                    if my_bullets_y[bullet_counter_for_now]<my_hitbox_y_max2:
                        my_bullets_x[bullet_counter_for_now]=-40
                        my_score+=1
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
def myothershipshootfunction():
    global my_bullet_vel2
    global clocktime2
    global for_now_clock2
    global shooting_unlock2
    global bullet_counter2
    global bullet_counter_for_now2
    global is_me_shooting2
    global my_bullets_x2
    global my_bullets_y2
    global shooting_Separator2
    global computer_hitbox_x_min2
    global computer_hitbox_x_max2
    global computer_hitbox_y_min2
    global computer_vel2
    global my_score2
    global my_x
    global my_y
    global my_x2
    global my_y2
    if my_y2>my_y-20 and my_y2<my_y+130:
        if not(is_me_shooting2):
            is_me_shooting2=True
            shooting_unlock2=False
            for_now_clock2=clocktime2+1
            bullet_counter2+=1
            if bullet_counter2==6:
                bullet_counter2=0
            bullet_counter_for_now2=bullet_counter2
            my_bullets_x2[bullet_counter_for_now2]=my_x2+120
            my_bullets_y2[bullet_counter_for_now2]=my_y2+60           
    if for_now_clock2==clocktime2:
        shooting_unlock2=True
    if is_me_shooting2:
        if my_bullets_x2[bullet_counter_for_now2]>my_hitbox_x_min:
            if my_bullets_x[bullet_counter_for_now2]<my_hitbox_x_max:
                if my_bullets_y2[bullet_counter_for_now2]>my_hitbox_y_min:
                    if my_bullets_y2[bullet_counter_for_now2]<my_hitbox_y_max:
                        my_bullets_x2[bullet_counter_for_now2]=840
                        my_score2+=1
        if my_bullets_x2[bullet_counter_for_now2]!=840:
            my_bullets_x2[bullet_counter_for_now2]+=my_bullet_vel2
            if my_bullets_x2[bullet_counter_for_now2]!=840:
                my_bullets_x2[0]==840
                my_bullets_x2[1]==840
                my_bullets_x2[2]==840
                my_bullets_x2[3]==840
                my_bullets_x2[4]==840
                my_bullets_x2[5]==840
        else:
            is_me_shooting2=False
#clock_tick
def clocktick():
    global clocktime
    global for_now_clock
    if clocktime==60:
        clocktime=0
    else:
        clocktime+=1
#clock_tick
def otherclocktick():
    global clocktime2
    global for_now_clock2
    if clocktime2==60:
        clocktime2=0
    else:
        clocktime2+=1
def updates():
    global my_hitbox_x_min
    global my_hitbox_x_max
    global my_hitbox_y_min
    global my_hitbox_y_max
    global my_x
    global my_y
    global my_hitbox_x_min2
    global my_hitbox_x_max2
    global my_hitbox_y_min2
    global my_hitbox_y_max2
    global my_x2
    global my_y2
    my_hitbox_x_min=my_x+50
    my_hitbox_x_max=my_x+120
    my_hitbox_y_min=my_y+40
    my_hitbox_y_max=my_y+100
    my_hitbox_x_min2=my_x2+50
    my_hitbox_x_max2=my_x2+120
    my_hitbox_y_min2=my_y2+60
    my_hitbox_y_max2=my_y2+100
#mainloop                                    
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event. type ==pygame.QUIT:
            run=False
    if my_score==10 or my_score2==10:
        run=False
            
        keys=pygame.key.get_pressed()
    updates()
    myshipmovement()
    myothershipmovement()
    myshipshootfunction()
    myothershipshootfunction()
    otherclocktick()
    clocktick()
    redrawgamewindow()
pygame.quit()
