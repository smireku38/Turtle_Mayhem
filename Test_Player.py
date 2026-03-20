import turtle

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(1300,700)
MB_locks={'MB1':True,'MB2':True,'MB3':True,'MB4':True}
player_movements={'up':False,'down':False,'left':False,'right':False,
                  'lock':True,'ani_ply':'down','ani_lcok':True,
                  'ani_count':20,'flap_speed':5, 'move_timer':-5, 'move_lock':True} #player movement locks
player = turtle.Turtle()
player.color('teal')
player.penup()

screen.register_shape('Kiki_UL.gif')
screen.register_shape('Kiki_DL.gif')
screen.register_shape('Kiki_UR.gif')
screen.register_shape('Kiki_DR.gif')
screen.register_shape('PT_FR.gif')
screen.register_shape('PT_FL.gif')
screen.register_shape('PT_FS.gif')
screen.register_shape('PT_BR.gif')
screen.register_shape('PT_BL.gif')
screen.register_shape('PT_BS.gif')
screen.register_shape('PT_LR.gif')
screen.register_shape('PT_LL.gif')
screen.register_shape('PT_LS.gif')
screen.register_shape('PT_RR.gif')
screen.register_shape('PT_RL.gif')
screen.register_shape('PT_RS.gif')


def player_animation():
    if player_movements['ani_ply']=='up':
        if player_movements['up']==True:
            if player_movements['move_timer']==-5:player.shape('PT_BL.gif')
            if player_movements['move_timer']==0:player.shape('PT_BS.gif')
            if player_movements['move_timer']==5:player.shape('PT_BR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_BS.gif')
            player_movements['move_timer']=-5
    if player_movements['ani_ply']=='down':
        if player_movements['down']==True:
            if player_movements['move_timer']==-5:player.shape('PT_FL.gif')
            if player_movements['move_timer']==0:player.shape('PT_FS.gif')
            if player_movements['move_timer']==5:player.shape('PT_FR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_FS.gif')
            player_movements['move_timer']=-5
    if player_movements['ani_ply']=='left':
        if player_movements['left']==True:
            if player_movements['move_timer']==-5:player.shape('PT_LL.gif')
            if player_movements['move_timer']==0:player.shape('PT_LS.gif')
            if player_movements['move_timer']==5:player.shape('PT_LR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_LS.gif')
            player_movements['move_timer']=-5
    if player_movements['ani_ply']=='right':
        if player_movements['right']==True:
            if player_movements['move_timer']==-5:player.shape('PT_RL.gif')
            if player_movements['move_timer']==0:player.shape('PT_RS.gif')
            if player_movements['move_timer']==5:player.shape('PT_RR.gif')
            if player_movements['move_lock']==True:
                if player_movements['move_timer']!=5:player_movements['move_timer']+=1
                else:player_movements['move_lock']=False
            if player_movements['move_lock']==False:
                if player_movements['move_timer']!=-5:player_movements['move_timer']-=1
                else:player_movements['move_lock']=True
        else:
            player.shape('PT_RS.gif')
            player_movements['move_timer']=-5

def press_up(): 
    player_movements['up']=True
    player_movements['down']=False
    player_movements['left']=False
    player_movements['right']=False
def release_up(): player_movements['up']=False
def press_down():
    player_movements['up']=False
    player_movements['down']=True
    player_movements['left']=False
    player_movements['right']=False
def release_down(): player_movements['down']=False
def press_left():
    player_movements['up']=False
    player_movements['down']=False
    player_movements['left']=True
    player_movements['right']=False
def release_left(): player_movements['left']=False
def press_right():
    player_movements['up']=False
    player_movements['down']=False
    player_movements['left']=False
    player_movements['right']=True
def release_right(): player_movements['right']=False

def move_game():
    player_animation()
    if player_movements['up']:
        if player_movements['ani_ply']!='up':player_movements['ani_ply']='up'
        player.sety(player.ycor()+3)
    if player_movements['down']:
        if player_movements['ani_ply']!='down':player_movements['ani_ply']='down'
        player.sety(player.ycor()-3)
    if player_movements['left']:
        if player_movements['ani_ply']!='left':player_movements['ani_ply']='left'
        player.setx(player.xcor()-3)
    if player_movements['right']:
        if player_movements['ani_ply']!='right':player_movements['ani_ply']='right'
        player.setx(player.xcor()+3)
    screen.update()
    screen.ontimer(move_game, 5)

if __name__ == '__main__':
    screen.listen()
    screen.onkeypress(press_up, 'w')
    screen.onkeyrelease(release_up, 'w')
    screen.onkeypress(press_down, 's')
    screen.onkeyrelease(release_down, 's')
    screen.onkeypress(press_left, 'a')
    screen.onkeyrelease(release_left, 'a')
    screen.onkeypress(press_right, 'd')
    screen.onkeyrelease(release_right, 'd')
    move_game()
    screen.mainloop()